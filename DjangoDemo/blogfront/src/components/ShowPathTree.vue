<template>
<div>
  <el-container>
    <el-aside>
      <el-scrollbar style="height:100%">
  <el-tree
    :data="folderTree"
    show-checkbox
    node-key="id"
    :default-expand-all="false"
    :expand-on-click-node="false"
    @node-click="handleSelect"
    @node-contextmenu="rightClick"
    :render-content="renderTree">
  </el-tree>
        </el-scrollbar>
      <div   v-show="menuVisible" @mouseleave="menuVisible=!menuVisible">
        <div id="menu" class="menu">
          <div><el-button type="text" icon="el-icon-plus" class="menu_item" @click="appendNode('testcases')">新建用例</el-button></div>
          <div><el-button type="text" icon="el-icon-plus" class="menu_item" @click="appendNode('keywords')">新建关键字</el-button></div>
          <div><el-button type="text" icon="el-icon-edit" class="menu_item">重命名</el-button></div>
          <div><el-button type="text" icon="el-icon-remove-outline" class="menu_item">删除</el-button></div>
        </div>
        <div id="folder_menu" class="folder_menu">
          <div><el-button type="text" icon="el-icon-plus" class="menu_item" @click="appendNode('testcases')">新建测试集</el-button></div>
          <div><el-button type="text" icon="el-icon-plus" class="menu_item" @click="appendNode('keywords')">新建文件夹</el-button></div>
          <div><el-button type="text" icon="el-icon-edit" class="menu_item">重命名</el-button></div>
          <div><el-button type="text" icon="el-icon-remove-outline" class="menu_item">删除</el-button></div>
        </div>
      </div>
    </el-aside>
  <el-container>
    <el-main>
      <div v-if="viewFileRaw === true">
        <el-scrollbar style="height:100%">
        <el-button style="float: left" type="primary" size="mini" @click="saveRawFile">save</el-button>
        <el-input
          v-model="currentFileContent"
          type="textarea"
          autosize
          placeholder="文件内容">
        </el-input>
          </el-scrollbar>
      </div>
      <div :hidden="hiddenFlag">
      <span v-if="currentObjType === 'testcases'" style="float: left; color: green">Test Case:{{currentTestCaseTitle}}</span>
        <span v-if="currentObjType === 'settings'" style="float: left; color: goldenrod">Settings:</span>
        <span v-if="currentObjType === 'variables'" style="float: left; color: darkseagreen" >Variable:</span>
        <span v-if="currentObjType === 'keywords'" style="float: left; color: green" >Keyword:{{currentTestCaseTitle}}</span>
        <show-test-case-content :content="testCaseContent" ref="testcaseTable" @viewUpdatedRaw="viewUpdatedRaw" @submit="saveTestCase"></show-test-case-content>
      </div>
    </el-main>
  </el-container>
  </el-container>

</div>
</template>

<script>
import ShowTestCaseContent from './ShowTestCaseContent'
import { findTypeEndIndex, putTestCaseIntoSuite, putFileInFolder, transferFolderToTree, transferListToFormatedRFCase, transferListToFormatedRFSettings, generateSuiteFile } from '../../lib/utils'
export default {
  name: 'ShowPathTree',
  components: { ShowTestCaseContent },
  data () {
    return {
      menuVisible: false,
      folderList: [],
      fileList: [],
      folderTree: [],
      fileContent: [],
      settings: [],
      testCases: [],
      testCaseContent: [[]],
      currentFileContent: '',
      currentTestCase: {},
      currentTestCaseTitle: '',
      currentObjType: '',
      currentNode: '',
      hiddenFlag: true,
      viewFileRaw: false,
      startFileId: 0,
      startFolderId: 0
    }
  },
  mounted () {
    this.getPathTree()
  },
  methods: {
    rightClick (MouseEvent, object, Node, element) {
      this.currentNode = Node
      console.log(this.currentNode.data.type)
      this.menuVisible = false
      this.menuVisible = true
      if (this.currentNode.data.type === 'folder') {
        let menu = document.querySelector('#folder_menu')
      } else {
        let menu = document.querySelector('#menu')
      }
      this.styleMenu(menu)
      // menu.style.cssText = 'position: fixed; left: ' + (MouseEvent.clientX - 5) + 'px' + '; top: ' + (MouseEvent.clientY - 10) + 'px; z-index: 999; cursor:pointer;'
    },
    foo () {
      // 取消鼠标监听事件 菜单栏
      this.menuVisible = false
      document.removeEventListener('click', this.foo) // 要及时关掉监听，不关掉的是一个坑，不信你试试，虽然前台显示的时候没有啥毛病，加一个alert你就知道了
    },
    styleMenu (menu) {
      if (event.clientX > 1800) {
        menu.style.left = event.clientX - 100 + 'px'
      } else {
        menu.style.left = event.clientX + 1 + 'px'
      }
      document.addEventListener('click', this.foo) // 给整个document新增监听鼠标事件，点击任何位置执行foo方法
      if (event.clientY > 700) {
        menu.style.top = event.clientY - 30 + 'px'
      } else {
        menu.style.top = event.clientY - 10 + 'px'
      }
    },
    saveRawFile () {
      let modifiedContent = ''
      this.$axios.post('/saveRawFile/', {
        rawData: this.currentFileContent,
        filePath: this.currentTestSuite.file_path
      }).then(resp => {
        if (resp && resp.status === 200) {
          this.$message({
            type: 'info',
            message: '已保存成功'
          })
          modifiedContent = resp.data.fileContent
          this.currentTestSuite.file_content = modifiedContent
          this.currentNode.parent.data.file_content = modifiedContent
          let children = putTestCaseIntoSuite(this.currentTestSuite)
          this.currentTestSuite.children = children
          this.currentNode.parent.data.children = children
        }
      })
    },
    saveTestCase (data) {
      this.updateCurrentData(data)
      this.$axios.post('/saveSuiteFile/', {
        suiteInfo: this.currentTestSuite
      }).then(resp => {
        if (resp && resp.status === 200) {
          this.$message({
            type: 'info',
            message: '已保存成功'
          })
        }
      }
      )
    },
    handleSelect (data, node, obj) {
      this.currentNode = node
      this.viewFileRaw = false
      this.hiddenFlag = true
      this.currentNode = node
      this.currentTestSuite = node.parent.data
      this.currentObjType = node.data.type
      if (this.currentObjType === 'file') {
        this.currentTestSuite = node.data
      }
      if (this.currentObjType === 'testcases' || this.currentObjType === 'keywords') {
        this.hiddenFlag = false
        this.currentTestCaseTitle = node.data.title
        this.testCaseContent = node.data.content
      } else if (this.currentObjType === 'settings') {
        this.hiddenFlag = false
        this.currentTestCaseTitle = 'settings'
        this.testCaseContent = node.data.content
      } else if (this.currentObjType === 'variables') {
        this.hiddenFlag = false
        this.currentTestCaseTitle = 'variables'
        this.testCaseContent = node.data.content
      } else {
        this.testCaseContent = [[]]
      }
      /* if (this.currentObjType === 'file') {
        this.showRaw()
      } */
    },
    viewUpdatedRaw (data) {
      this.updateCurrentData(data)
      this.hiddenFlag = true
      this.viewFileRaw = true
      this.currentFileContent = generateSuiteFile(this.currentTestSuite)
    },
    updateCurrentData (data) {
      console.log(data)
      if (this.currentObjType === 'testcases') {
        var testCases = this.currentTestSuite.file_content.testcases
        for (let index in testCases) {
          if (testCases[index].title === this.currentTestCaseTitle) {
            testCases[index].content = transferListToFormatedRFCase(data)
            this.currentTestSuite.children[index].content = data
            break
          }
        }
        this.currentTestSuite.file_content.testcases = testCases
      }
      if (this.currentObjType === 'keywords') {
        var keywords = this.currentTestSuite.file_content.keywords
        for (let index in keywords) {
          if (keywords[index].title === this.currentTestCaseTitle) {
            console.log(this.currentTestCaseTitle)
            keywords[index].content = transferListToFormatedRFCase(data)
            this.currentTestSuite.children[index].content = data
            break
          }
        }
        this.currentTestSuite.file_content.keywords = keywords
      }
      if (this.currentObjType === 'settings') {
        var updateSettings = transferListToFormatedRFSettings(data)
        for (let item in this.currentTestSuite.children) {
          if (this.currentTestSuite.children[item].type === 'settings') {
            this.currentTestSuite.children[item].content = data
            break
          }
        }
        this.currentTestSuite.file_content.settings = updateSettings
      }
      if (this.currentObjType === 'variables') {
        var updateVariables = transferListToFormatedRFSettings(data)
        for (let item in this.currentTestSuite.children) {
          if (this.currentTestSuite.children[item].type === 'variables') {
            this.currentTestSuite.children[item].content = data
            break
          }
        }
        this.currentTestSuite.file_content.variables = updateVariables
      }
    },
    showRaw () {
      this.hiddenFlag = true
      this.viewFileRaw = true
      this.currentFileContent = generateSuiteFile(this.currentTestSuite)
    },
    getPathTree () {
      this.$axios.get('/getFileTreeList/').then(resp => {
        if (resp && resp.status === 200) {
          const resps = JSON.parse(JSON.stringify(resp))
          this.fileList = resps.data.files
          this.startFileId = this.fileList.length + 1
          this.startFolderId = this.fileList.length + 1
          this.folderList = resps.data.folders
          this.folderTree = transferFolderToTree(putFileInFolder(this.folderList, this.fileList))
        }
      })
    },
    renderTree (h, {node, data, store}) {
      // if (!data.type) { // === 'folder' || data.type === 'file') {
      if (data.type === 'folder' || data.type === 'file') {
        return (
          <span class="treeItem">
            <span style="margin-right:5px">{data.label}</span>
            <span>
              <el-button size="medium" icon="el-icon-circle-plus-outline" type="text" on-click={ () => this.appendNode(node, data) }></el-button>
            </span>
          </span>
          /* <div class="treeItem">
            <span>
              <i class={data.icon} style="margin-right:5px; color: yellowgreen; font-weight: bold"></i>
              {data.label}
            </span>
            <span>
              <el-button on-click={this.addNode} type="text" icon="el-icon-circle-plus-outline" circle></el-button>
            </span>
          </div> */
        )
      } else {
        return (
          <div class="treeItem">
            <i class={data.icon} style="margin-right:5px; color: yellowgreen; font-weight: bold"></i>
            {data.label}
          </div>
        /*  <span class="treeItem">
            <span style="margin-right:5px">{data.label}</span>
            <span>
              <el-button size="medium" icon="el-icon-circle-plus-outline" type="text" on-click={ () => this.appendNode(node, data) }></el-button>
            </span>
          </span> */
        )
      }
    },
    appendNode (type) {
      console.log(type)
      console.log(this.currentNode)
      if (type === 'testcases') {
        this.$prompt('用例名称', '新建', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          inputPattern: /.*/,
          inputErrorMessage: '名称不正确'
        }).then(({value}) => {
          let content = new Array(['', '', ''])
          let testCaseEndIndex = findTypeEndIndex(this.currentNode.data.children)
          console.log(testCaseEndIndex)
          this.currentNode.data.children.splice(testCaseEndIndex, 0, {
            'content': content,
            'icon': 'el-icon-reading',
            'label': value,
            'name': value,
            'title': value,
            'type': 'testcases'
          })
          console.log(this.currentTestSuite)
          this.currentTestSuite.file_content.testcases.push({'content': content, 'title': value})
          this.$message({
            type: 'success',
            message: '创建成功'
          })
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '取消'
          })
        })
      } else if (type === 'keywords') {
        this.$prompt('关键字名称', '新建', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          inputPattern: /.*/,
          inputErrorMessage: '名称不正确'
        }).then(({value}) => {
          let content = new Array(['', '', ''])
          this.currentNode.data.children.push({
            'content': content,
            'icon': 'el-icon-setting',
            'label': value,
            'name': value,
            'title': value,
            'type': 'keywords'
          })
          console.log(this.currentTestSuite)
          this.currentTestSuite.file_content.keywords.push({'content': content, 'title': value})
          // this.currentTestSuite = this.currentNode.data
          // this.viewUpdatedRaw(this.currentNode.data)
          /* var id = 0
        console.log('before add: ' + this.startFolderId)

        if (data.type === 'folder') {
          id = this.startFolderId++
        } else {
          id = this.startFileId++
        }
        console.log('after add: ' + this.startFolderId)
        const newChild = { id: id, label: 'test', children: [] }
        console.log('after add: ' + id)
        if (!data.children) {
          this.$set(data, 'children', [])
        }
        data.children.push(newChild) */
          this.$message({
            type: 'success',
            message: '创建成功'
          })
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '取消'
          })
        })
      }
      /* var id = 0
      console.log('before add: ' + this.startFolderId)
      if (data.type === 'folder') {
        id = this.startFolderId++
      } else {
        id = this.startFileId++
      }
      console.log('after add: ' + this.startFolderId)
      const newChild = { id: id, label: 'test', children: [] }
      console.log('after add: ' + id)
      if (!data.children) {
        this.$set(data, 'children', [])
      }
      data.children.push(newChild) */
    },
    addNewCase () {
      this.$prompt('用例名称', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        inputPattern: /.*/,
        inputErrorMessage: '用例名称不正确'
      }).then(({value}) => {
        this.$message({
          type: 'success',
          message: '创建成功'
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '取消'
        })
      })
    }
  }
}
</script>

<style>
.treeItem {
  display: inline-block;
  width: ~"calc(100% - 50px)";
  color: black;
  height: 60px;
  line-height: 60px;
}
.el-icon-folder {
  }
.el-scrollbar__wrap {
  overflow-x: hidden;
  height: 800px;
}
.menu__item {
  display: block;
  line-height: 20px;
  text-align: center;
  margin:10px;
  cursor: default;
}
.menu__item:hover{
  color: #FF0000;
}
.menu {
  height: auto;
  width: auto;
  position: absolute;
  font-size: 14px;
  text-align: left;
  border-radius: 10px;
  border: 1px solid #c1c1c1;
  background-color: #ffffff;
}

li:hover {
  background-color: #E0E0E2;
  color: white;
}
</style>
