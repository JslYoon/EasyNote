console.log('from background')

console.log(window.location.href)
chrome.tabs.onActivated.addListener(tab =>  {
    chrome.tabs.get(tab.tabId, current_tab_info => {
    console.log(current_tab_info.url)
    
    //chrome.tabs.executeScript(null, {file: './foreground.js'}, () => console.log('i.injected'))
    localStorage.setItem("vOneLocalStorage", current_tab_info.url);
    })
});



