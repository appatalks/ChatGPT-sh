javascript: (function () {
    var filename = document.title;
    var html = document.documentElement.outerHTML;
    var blob = new Blob([html], {type: "text/html"});
    var url = URL.createObjectURL(blob);
    var a = document.createElement("a");
    a.href = url;
    a.download = filename + ".html";
    a.click();
})();
