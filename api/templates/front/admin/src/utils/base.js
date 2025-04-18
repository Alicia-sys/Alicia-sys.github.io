const base = {
    get() {
        return {
            url : "http://localhost:8080/pythonek97261k/",
            name: "pythonek97261k",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/dist/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "基于Python人脸识别的智能实验室门禁管理系统"
        } 
    }
}
export default base
