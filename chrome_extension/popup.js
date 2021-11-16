document.addEventListener('DOMContentLoaded', function() {
    chrome.tabs.query({'active': true, 'windowId': chrome.windows.WINDOW_ID_CURRENT},
        function(tabs){
            alert(tabs[0].url);
        })
}
)
alert('hello')

// chrome.tabs.onUpdated.addListener( function (tabId, changeInfo, tab) {
//     if (changeInfo.status == 'complete' && tab.active) {
  
//         alert(tab.url);
  
//     }
//   })