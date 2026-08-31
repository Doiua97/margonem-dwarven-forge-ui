# Client JS layout analysis

- Archive: `docs/main.min.53XkBRxF.zip`
- JS entry: `main.min.53XkBRxF.js`
- JS bytes: 3019667
- Characters: 3019349

## inline-style
Matches: **81**

### 1
```js
lt`,scroll:!0,scrollSensitivity:20,scrollSpeed:20,snap:!1,snapMode:`both`,snapTolerance:20,stack:!1,zIndex:!1,drag:null,start:null,stop:null},_create:function(){this.options.helper!==`original`||/^(?:r|a|f)/.test(this.element.css(`position`))||(this.element[0].style.position=`relative`),this.options.addClasses&&this.element.addClass(`ui-draggable`),this.options.disabled&&this.element.addClass(`ui-draggable-disabled`),this._setHandleClassName(),this._mouseInit()},_setOption:function(t,n){this._super(t,n),t===`handle`&&(this._removeHandleClassName(),this._setHandleClassName())},_destroy:function(){(this.helper||this.element).is(`
```
### 2
```js
arent=this._getParentOffset()),this.position=this._generatePosition(n,!0),this.positionAbs=this._convertPositionTo(`absolute`),!r){var i=this._uiHash();if(this._trigger(`drag`,n,i)===!1)return this._mouseUp({}),!1;this.position=i.position}return this.helper[0].style.left=this.position.left+`px`,this.helper[0].style.top=this.position.top+`px`,t.ui.ddmanager&&t.ui.ddmanager.drag(this,n),!1},_mouseStop:function(n){var r=this,i=!1;return t.ui.ddmanager&&!this.options.dropBehaviour&&(i=t.ui.ddmanager.drop(this,n)),this.dropped&&(i=this.dropped,this.dropped=!1),this.options.revert===`invalid`&&!i||this.options.revert===`valid`&&i
```
### 3
```js
_generatePosition(n,!0),this.positionAbs=this._convertPositionTo(`absolute`),!r){var i=this._uiHash();if(this._trigger(`drag`,n,i)===!1)return this._mouseUp({}),!1;this.position=i.position}return this.helper[0].style.left=this.position.left+`px`,this.helper[0].style.top=this.position.top+`px`,t.ui.ddmanager&&t.ui.ddmanager.drag(this,n),!1},_mouseStop:function(n){var r=this,i=!1;return t.ui.ddmanager&&!this.options.dropBehaviour&&(i=t.ui.ddmanager.drop(this,n)),this.dropped&&(i=this.dropped,this.dropped=!1),this.options.revert===`invalid`&&!i||this.options.revert===`valid`&&i||this.options.revert===!0||t.isFunction(this.opt
```
### 4
```js
l=t(document).scrollLeft(t(document).scrollLeft()+c.scrollSpeed))),l!==!1&&t.ui.ddmanager&&!c.dropBehaviour&&t.ui.ddmanager.prepareOffsets(this,n)),this.positionAbs=this._convertPositionTo(`absolute`),this.options.axis&&this.options.axis===`y`||(this.helper[0].style.left=this.position.left+`px`),this.options.axis&&this.options.axis===`x`||(this.helper[0].style.top=this.position.top+`px`),r=this.items.length-1;r>=0;r--)if(i=this.items[r],a=i.item[0],s=this._intersectsWithPointer(i),s&&i.instance===this.currentContainer&&a!==this.currentItem[0]&&this.placeholder[s===1?`next`:`prev`]()[0]!==a&&!t.contains(this.placeholder[0],a
```
### 5
```js
opBehaviour&&t.ui.ddmanager.prepareOffsets(this,n)),this.positionAbs=this._convertPositionTo(`absolute`),this.options.axis&&this.options.axis===`y`||(this.helper[0].style.left=this.position.left+`px`),this.options.axis&&this.options.axis===`x`||(this.helper[0].style.top=this.position.top+`px`),r=this.items.length-1;r>=0;r--)if(i=this.items[r],a=i.item[0],s=this._intersectsWithPointer(i),s&&i.instance===this.currentContainer&&a!==this.currentItem[0]&&this.placeholder[s===1?`next`:`prev`]()[0]!==a&&!t.contains(this.placeholder[0],a)&&(this.options.type!==`semi-dynamic`||!t.contains(this.element[0],a))){if(this.direction=s===
```
### 6
```js
tem])):r.helper===`clone`?this.currentItem.clone():this.currentItem;return i.parents(`body`).length||t(r.appendTo===`parent`?this.currentItem[0].parentNode:r.appendTo)[0].appendChild(i[0]),i[0]===this.currentItem[0]&&(this._storedCSS={width:this.currentItem[0].style.width,height:this.currentItem[0].style.height,position:this.currentItem.css(`position`),top:this.currentItem.css(`top`),left:this.currentItem.css(`left`)}),(!i[0].style.width||r.forceHelperSize)&&i.width(this.currentItem.width()),(!i[0].style.height||r.forceHelperSize)&&i.height(this.currentItem.height()),i},_adjustOffsetFromHelper:function(n){typeof n==`string`&
```
### 7
```js
tem.clone():this.currentItem;return i.parents(`body`).length||t(r.appendTo===`parent`?this.currentItem[0].parentNode:r.appendTo)[0].appendChild(i[0]),i[0]===this.currentItem[0]&&(this._storedCSS={width:this.currentItem[0].style.width,height:this.currentItem[0].style.height,position:this.currentItem.css(`position`),top:this.currentItem.css(`top`),left:this.currentItem.css(`left`)}),(!i[0].style.width||r.forceHelperSize)&&i.width(this.currentItem.width()),(!i[0].style.height||r.forceHelperSize)&&i.height(this.currentItem.height()),i},_adjustOffsetFromHelper:function(n){typeof n==`string`&&(n=n.split(` `)),t.isArray(n)&&(n={left
```
### 8
```js
].appendChild(i[0]),i[0]===this.currentItem[0]&&(this._storedCSS={width:this.currentItem[0].style.width,height:this.currentItem[0].style.height,position:this.currentItem.css(`position`),top:this.currentItem.css(`top`),left:this.currentItem.css(`left`)}),(!i[0].style.width||r.forceHelperSize)&&i.width(this.currentItem.width()),(!i[0].style.height||r.forceHelperSize)&&i.height(this.currentItem.height()),i},_adjustOffsetFromHelper:function(n){typeof n==`string`&&(n=n.split(` `)),t.isArray(n)&&(n={left:+n[0],top:+n[1]||0}),`left`in n&&(this.offset.click.left=n.left+this.margins.left),`right`in n&&(this.offset.click.left=this.hel
```
### 9
```js
is.currentItem[0].style.width,height:this.currentItem[0].style.height,position:this.currentItem.css(`position`),top:this.currentItem.css(`top`),left:this.currentItem.css(`left`)}),(!i[0].style.width||r.forceHelperSize)&&i.width(this.currentItem.width()),(!i[0].style.height||r.forceHelperSize)&&i.height(this.currentItem.height()),i},_adjustOffsetFromHelper:function(n){typeof n==`string`&&(n=n.split(` `)),t.isArray(n)&&(n={left:+n[0],top:+n[1]||0}),`left`in n&&(this.offset.click.left=n.left+this.margins.left),`right`in n&&(this.offset.click.left=this.helperProportions.width-n.right+this.margins.left),`top`in n&&(this.offset.cli
```
### 10
```js
:null,resizeStop:null},sizeRelatedOptions:{buttons:!0,height:!0,maxHeight:!0,maxWidth:!0,minHeight:!0,minWidth:!0,width:!0},resizableRelatedOptions:{maxHeight:!0,maxWidth:!0,minHeight:!0,minWidth:!0},_create:function(){this.originalCss={display:this.element[0].style.display,width:this.element[0].style.width,minHeight:this.element[0].style.minHeight,maxHeight:this.element[0].style.maxHeight,height:this.element[0].style.height},this.originalPosition={parent:this.element.parent(),index:this.element.parent().children().index(this.element)},this.originalTitle=this.element.attr(`title`),this.options.title=this.options.title||this.or
```
### 11
```js
tions:{buttons:!0,height:!0,maxHeight:!0,maxWidth:!0,minHeight:!0,minWidth:!0,width:!0},resizableRelatedOptions:{maxHeight:!0,maxWidth:!0,minHeight:!0,minWidth:!0},_create:function(){this.originalCss={display:this.element[0].style.display,width:this.element[0].style.width,minHeight:this.element[0].style.minHeight,maxHeight:this.element[0].style.maxHeight,height:this.element[0].style.height},this.originalPosition={parent:this.element.parent(),index:this.element.parent().children().index(this.element)},this.originalTitle=this.element.attr(`title`),this.options.title=this.options.title||this.originalTitle,this._createWrapper(),
```
### 12
```js
ght:!0,maxWidth:!0,minHeight:!0,minWidth:!0},_create:function(){this.originalCss={display:this.element[0].style.display,width:this.element[0].style.width,minHeight:this.element[0].style.minHeight,maxHeight:this.element[0].style.maxHeight,height:this.element[0].style.height},this.originalPosition={parent:this.element.parent(),index:this.element.parent().children().index(this.element)},this.originalTitle=this.element.attr(`title`),this.options.title=this.options.title||this.originalTitle,this._createWrapper(),this.element.show().removeAttr(`title`).addClass(`ui-dialog-content ui-widget-content`).appendTo(this.uiDialog),this._cr
```
### 13
```js
ng.socket_enchantment||Engine.crafting.socket_extraction||Engine.crafting.socket_composition),getMoveItemTranslation=()=>_t(`move`,null,`item`),getHeroLevel$1=()=>Engine.hero?Engine.hero.getLevel():0,addTooltip=(t,n)=>{$(t).tip(n)},setDisplayProperty=(t,n)=>{t.style.display=n?`block`:`none`},confirmWithCallback$1=({msg:t,clb:n,accept:r=_t(`yes`),cancel:i=_t(`no`)})=>{mAlert(t,[{txt:r,callback:()=>(typeof n==`function`&&n(),!0)},{txt:i,callback:()=>!0}])},createElement=(t,n)=>{let r=document.createElement(t);if(!n)return r;n.id&&(r.id=n.id),n.className&&(Array.isArray(n.className)?r.classList.add(...n.className):r.className=n.c
```
### 14
```js
+n,m:`no-quit`})},window.isOwnItem=isOwnItem$1,window.notOwnItem=function(t,n){return!isOwnItem$1(n)&&(Engine.items.deleteItem(t),Engine.trade?(Engine.trade.removeTradeItem(t),!0):!1)},window.copyClipboard=function(t){var n=document.createElement(`textarea`);n.style.position=`absolute`,n.style.opacity=`0`,n.value=t,document.body.appendChild(n),n.select();try{document.execCommand(`copy`)}catch{console.log(`Your browser doesn't support copy button`)}document.body.removeChild(n)},window.mAlert=function(t,n,r,i){if(isSameAlertExist(t))return;i?console.log(i):i=o$19.$_M_ALERT_LAYER;let a;switch(i){case o$19.$_M_ALERT_LAYER:a=Engine.
```
### 15
```js
ick`,!0),isset(t.tip)&&n.tip(t.tip),t.isRed&&n.addClass(`option--red`),isset(t.icon)&&L(n,t),isset(t.remove)&&P(t.remove)&&F(n,t),n}function z(){if(_)return;_=!0,C.addClass(`close-menu`),b.detach(),b.appendTo(h),b.show(),me(),b.hide();let t=O,n=parseFloat(b[0].style.top);b[0].style.height=`0px`,b[0].style.overflow=`hidden`,D&&(b[0].style.top=n+t+`px`),b.show();let r={height:t};D&&(r.top=n),b.animate(r,{duration:`fast`,start:function(){m!==null&&m.addClass(`selected`),$(s).on(`close`,H),$(window).on(`mousedown`,B),$(window).on(`touchstart`,B),$(window).on(`mousewheel`,H),$(window).on(`resize`,me)},complete:function(){b[0].s
```
### 16
```js
.tip)&&n.tip(t.tip),t.isRed&&n.addClass(`option--red`),isset(t.icon)&&L(n,t),isset(t.remove)&&P(t.remove)&&F(n,t),n}function z(){if(_)return;_=!0,C.addClass(`close-menu`),b.detach(),b.appendTo(h),b.show(),me(),b.hide();let t=O,n=parseFloat(b[0].style.top);b[0].style.height=`0px`,b[0].style.overflow=`hidden`,D&&(b[0].style.top=n+t+`px`),b.show();let r={height:t};D&&(r.top=n),b.animate(r,{duration:`fast`,start:function(){m!==null&&m.addClass(`selected`),$(s).on(`close`,H),$(window).on(`mousedown`,B),$(window).on(`touchstart`,B),$(window).on(`mousewheel`,H),$(window).on(`resize`,me)},complete:function(){b[0].style.height=``,b[0]
```
### 17
```js
set(t.icon)&&L(n,t),isset(t.remove)&&P(t.remove)&&F(n,t),n}function z(){if(_)return;_=!0,C.addClass(`close-menu`),b.detach(),b.appendTo(h),b.show(),me(),b.hide();let t=O,n=parseFloat(b[0].style.top);b[0].style.height=`0px`,b[0].style.overflow=`hidden`,D&&(b[0].style.top=n+t+`px`),b.show();let r={height:t};D&&(r.top=n),b.animate(r,{duration:`fast`,start:function(){m!==null&&m.addClass(`selected`),$(s).on(`close`,H),$(window).on(`mousedown`,B),$(window).on(`touchstart`,B),$(window).on(`mousewheel`,H),$(window).on(`resize`,me)},complete:function(){b[0].style.height=``,b[0].style.overflow=``,me(),v.trigger(`update`),m!==null&&
```
### 18
```js
={height:t};D&&(r.top=n),b.animate(r,{duration:`fast`,start:function(){m!==null&&m.addClass(`selected`),$(s).on(`close`,H),$(window).on(`mousedown`,B),$(window).on(`touchstart`,B),$(window).on(`mousewheel`,H),$(window).on(`resize`,me)},complete:function(){b[0].style.height=``,b[0].style.overflow=``,me(),v.trigger(`update`),m!==null&&v.trigger(`setScroll`,[m[0].offsetTop-3])}})}function B(t){ee(t.target)||V()}function V(t){he(),b.stop(!0);let n=function(){_=!1,b[0].style.height=``,b[0].style.overflow=``,b.detach(),b.hide(),x.append(b),C.removeClass(`close-menu`)},r=parseFloat(b[0].style.top),i=b.outerHeight()||O;b[0].style.ove
```
### 19
```js
,$(window).on(`resize`,me)},complete:function(){b[0].style.height=``,b[0].style.overflow=``,me(),v.trigger(`update`),m!==null&&v.trigger(`setScroll`,[m[0].offsetTop-3])}})}function B(t){ee(t.target)||V()}function V(t){he(),b.stop(!0);let n=function(){_=!1,b[0].style.height=``,b[0].style.overflow=``,b.detach(),b.hide(),x.append(b),C.removeClass(`close-menu`)},r=parseFloat(b[0].style.top),i=b.outerHeight()||O;b[0].style.overflow=`hidden`;let a={height:0};D&&(a.top=r+i),b.animate(a,{duration:`fast`,complete:n})}function H(t){he(),b.stop(!0),b.hide(),_=!1,b.detach(),x.append(b),C.removeClass(`close-menu`)}function U(t){m=t;let n=
```
### 20
```js
!==null&&v.trigger(`setScroll`,[m[0].offsetTop-3])}})}function B(t){ee(t.target)||V()}function V(t){he(),b.stop(!0);let n=function(){_=!1,b[0].style.height=``,b[0].style.overflow=``,b.detach(),b.hide(),x.append(b),C.removeClass(`close-menu`)},r=parseFloat(b[0].style.top),i=b.outerHeight()||O;b[0].style.overflow=`hidden`;let a={height:0};D&&(a.top=r+i),b.animate(a,{duration:`fast`,complete:n})}function H(t){he(),b.stop(!0),b.hide(),_=!1,b.detach(),x.append(b),C.removeClass(`close-menu`)}function U(t){m=t;let n=s.find(`.menu-option`),r=t.attr(`selectedText`)||t.find(`.text`).html();X(),n.html(r),n.attr(`value`,t.attr(`value`
```
### 21
```js
=t[r];if(i.id==n){removeFromArray(t,i);return}}}function pe(t){let n=i.addNewOption.menuToAddAndRemove;for(let r in n){let i=n[r];if(i.id==t){removeFromArray(n,i);return}}}function me(){let t=s[0],n=b[0],r=y[0].querySelector(`.bck-wrapper`),i=t.offsetWidth-8;n.style.width=i+`px`;let a=t.getBoundingClientRect(),c=Math.min(r.offsetHeight,y[0].offsetHeight),l=Engine.zoomFactor,u=window.innerHeight/l,f=window.innerWidth/l,p=a.top/l,m=a.bottom/l,h=u-m,_=p;O=c;let v;h>=c||h>=_?(D=!1,v=Math.min(m,u-c)):(D=!0,v=Math.max(0,p-c-6));let x=Math.min(Math.max(0,(a.left+5)/l-3),Math.max(0,f-i));n.style.top=Math.round(v)+`px`,n.style.left=M
```
### 22
```js
setHeight,y[0].offsetHeight),l=Engine.zoomFactor,u=window.innerHeight/l,f=window.innerWidth/l,p=a.top/l,m=a.bottom/l,h=u-m,_=p;O=c;let v;h>=c||h>=_?(D=!1,v=Math.min(m,u-c)):(D=!0,v=Math.max(0,p-c-6));let x=Math.min(Math.max(0,(a.left+5)/l-3),Math.max(0,f-i));n.style.top=Math.round(v)+`px`,n.style.left=Math.round(x)+`px`}function he(){$(window).off(`mousedown`,B),$(window).off(`touchstart`,B),$(window).off(`mousewheel`,H),$(window).off(`resize`,me)}function ge(){s.find(`.arrow`).css(`display`,`block`)}function _e(){s.find(`.arrow`).css(`display`,`none`)}function ve(){s.find(`.reset`).css(`display`,`block`)}function ye(){s.f
```
### 23
```js
Engine.zoomFactor,u=window.innerHeight/l,f=window.innerWidth/l,p=a.top/l,m=a.bottom/l,h=u-m,_=p;O=c;let v;h>=c||h>=_?(D=!1,v=Math.min(m,u-c)):(D=!0,v=Math.max(0,p-c-6));let x=Math.min(Math.max(0,(a.left+5)/l-3),Math.max(0,f-i));n.style.top=Math.round(v)+`px`,n.style.left=Math.round(x)+`px`}function he(){$(window).off(`mousedown`,B),$(window).off(`touchstart`,B),$(window).off(`mousewheel`,H),$(window).off(`resize`,me)}function ge(){s.find(`.arrow`).css(`display`,`block`)}function _e(){s.find(`.arrow`).css(`display`,`none`)}function ve(){s.find(`.reset`).css(`display`,`block`)}function ye(){s.find(`.reset`).css(`display`,`non
```
### 24
```js
llable`)):($(a).removeClass(`scrollable`),i.addScrollableClassToAnotherEl&&i.addScrollableClassToAnotherEl.removeClass(`scrollable`)),c&&T(1)},C=function(t){let n=u[0],r=$(`.handle`,u)[0];if(!i.track)return;let a=Math.round((n.clientHeight-r.clientHeight)*t);r.style.top=a+`px`},w=!0,T=function(t){let n=s[0];n.scrollTop=Math.round((n.scrollHeight-n.clientHeight)*t),c=t>.99,C(t),c&&isset$3(i.callback)&&w?(i.callback(),w=!1):c!=1&&(w=!0)},D=function(){p&&(clearTimeout(p),p=null),f&&(clearInterval(f),f=null)},O=function(t){$(a).find(t).mouseleave(function(){D()}).mouseup(function(){D()})},k=function(t,n){$(a).find(t).mousedown
```
### 25
```js
,t.id-this.getWidth(),t.id+this.getWidth()],r=[];for(var i in n){var a=n[i],s=this.nodes[a];isset(s)&&t.isNeighbor(s)&&r.push(s)}return r},BaseMap.prototype.generateMap=function(){var t=this;let n=document.createElement(`canvas`);document.body.appendChild(n),n.style.position=`absolute`,n.style.top=`0`,n.style.left=`0`,n.style.zIndex=`10`;var r=()=>{let i=8;n.width=this.width*8+(this.chunksInRow-1)*8/2,n.height=this.height*8+(this.chunksRows-1)*8/2;let a=n.getContext(`2d`);for(var s in a.fillStyle=`white`,a.fillRect(0,0,n.width,n.height),t.chunks)t.chunks[s].draw(a,8);requestAnimationFrame(r)};requestAnimationFrame(r)};var Searc
```
### 26
```js
his.getWidth()],r=[];for(var i in n){var a=n[i],s=this.nodes[a];isset(s)&&t.isNeighbor(s)&&r.push(s)}return r},BaseMap.prototype.generateMap=function(){var t=this;let n=document.createElement(`canvas`);document.body.appendChild(n),n.style.position=`absolute`,n.style.top=`0`,n.style.left=`0`,n.style.zIndex=`10`;var r=()=>{let i=8;n.width=this.width*8+(this.chunksInRow-1)*8/2,n.height=this.height*8+(this.chunksRows-1)*8/2;let a=n.getContext(`2d`);for(var s in a.fillStyle=`white`,a.fillRect(0,0,n.width,n.height),t.chunks)t.chunks[s].draw(a,8);requestAnimationFrame(r)};requestAnimationFrame(r)};var SearchPathMap=function(t){Ba
```
### 27
```js
r=[];for(var i in n){var a=n[i],s=this.nodes[a];isset(s)&&t.isNeighbor(s)&&r.push(s)}return r},BaseMap.prototype.generateMap=function(){var t=this;let n=document.createElement(`canvas`);document.body.appendChild(n),n.style.position=`absolute`,n.style.top=`0`,n.style.left=`0`,n.style.zIndex=`10`;var r=()=>{let i=8;n.width=this.width*8+(this.chunksInRow-1)*8/2,n.height=this.height*8+(this.chunksRows-1)*8/2;let a=n.getContext(`2d`);for(var s in a.fillStyle=`white`,a.fillRect(0,0,n.width,n.height),t.chunks)t.chunks[s].draw(a,8);requestAnimationFrame(r)};requestAnimationFrame(r)};var SearchPathMap=function(t){BaseMap.call(this,t
```
### 28
```js
 n){var a=n[i],s=this.nodes[a];isset(s)&&t.isNeighbor(s)&&r.push(s)}return r},BaseMap.prototype.generateMap=function(){var t=this;let n=document.createElement(`canvas`);document.body.appendChild(n),n.style.position=`absolute`,n.style.top=`0`,n.style.left=`0`,n.style.zIndex=`10`;var r=()=>{let i=8;n.width=this.width*8+(this.chunksInRow-1)*8/2,n.height=this.height*8+(this.chunksRows-1)*8/2;let a=n.getContext(`2d`);for(var s in a.fillStyle=`white`,a.fillRect(0,0,n.width,n.height),t.chunks)t.chunks[s].draw(a,8);requestAnimationFrame(r)};requestAnimationFrame(r)};var SearchPathMap=function(t){BaseMap.call(this,t.x,t.y,8);for(var n
```
### 29
```js
();r.addEventListener(s,()=>{r.classList.contains(`disabled`)||(n.initAction?n.initAction():this.activateCard(t))})}updateAmount(t,n){let r=this.cards[t];if(!r||!r.amount)return;let i=this.getCard(t).querySelector(`.amount`);i&&(n>0||(r.amount.showZero??!1)?(i.style.display=`block`,i.innerHTML=r.amount.template?r.amount.template.replace(`%value%`,n.toString()):n.toString()):i.style.display=`none`)}disableTab(t,n){let r=this.getCard(t);if(r&&(r.classList.add(`disabled`),this.cards[t].disabled=!0,n&&($(r).tip(n),this.cards[t].disabledTip=n),this.currentTab===t)){let t=this.getFirstAvailableCard();t&&this.activateCard(t)}}enableT
```
### 30
```js
dateAmount(t,n){let r=this.cards[t];if(!r||!r.amount)return;let i=this.getCard(t).querySelector(`.amount`);i&&(n>0||(r.amount.showZero??!1)?(i.style.display=`block`,i.innerHTML=r.amount.template?r.amount.template.replace(`%value%`,n.toString()):n.toString()):i.style.display=`none`)}disableTab(t,n){let r=this.getCard(t);if(r&&(r.classList.add(`disabled`),this.cards[t].disabled=!0,n&&($(r).tip(n),this.cards[t].disabledTip=n),this.currentTab===t)){let t=this.getFirstAvailableCard();t&&this.activateCard(t)}}enableTab(t){let n=this.getCard(t);n&&(n.classList.remove(`disabled`),this.cards[t].disabled=!1,this.cards[t].disabledTip=voi
```
### 31
```js
.height=t.height()},A=t=>{if(j())for(let n in s)s[n].update(t)},j=()=>{if(!l)return!1;for(let t in s)if(s[t].getActive())return!0;return!1},M=()=>{l&&l.clearRect(0,0,c.width,c.height)},P=()=>{if(!j()){l&&F();return}I(),M();for(let t in s)s[t].draw(l)},F=()=>{c.style.display!=`none`&&(c.style.display=`none`)},I=()=>{c.style.display!=`block`&&(c.style.display=`block`)},L=(t,a,s)=>{Engine.colorInterfaceNotificationManager.checkNotificationExist(t)&&Engine.colorInterfaceNotificationManager.updateData({action:r,id:t}),Engine.colorInterfaceNotificationManager.updateData({action:n,id:t,color:a,blur:s}),Engine.colorInterfaceNotificati
```
### 32
```js
if(j())for(let n in s)s[n].update(t)},j=()=>{if(!l)return!1;for(let t in s)if(s[t].getActive())return!0;return!1},M=()=>{l&&l.clearRect(0,0,c.width,c.height)},P=()=>{if(!j()){l&&F();return}I(),M();for(let t in s)s[t].draw(l)},F=()=>{c.style.display!=`none`&&(c.style.display=`none`)},I=()=>{c.style.display!=`block`&&(c.style.display=`block`)},L=(t,a,s)=>{Engine.colorInterfaceNotificationManager.checkNotificationExist(t)&&Engine.colorInterfaceNotificationManager.updateData({action:r,id:t}),Engine.colorInterfaceNotificationManager.updateData({action:n,id:t,color:a,blur:s}),Engine.colorInterfaceNotificationManager.updateData({acti
```
### 33
```js
e(t)},j=()=>{if(!l)return!1;for(let t in s)if(s[t].getActive())return!0;return!1},M=()=>{l&&l.clearRect(0,0,c.width,c.height)},P=()=>{if(!j()){l&&F();return}I(),M();for(let t in s)s[t].draw(l)},F=()=>{c.style.display!=`none`&&(c.style.display=`none`)},I=()=>{c.style.display!=`block`&&(c.style.display=`block`)},L=(t,a,s)=>{Engine.colorInterfaceNotificationManager.checkNotificationExist(t)&&Engine.colorInterfaceNotificationManager.updateData({action:r,id:t}),Engine.colorInterfaceNotificationManager.updateData({action:n,id:t,color:a,blur:s}),Engine.colorInterfaceNotificationManager.updateData({action:i,id:t})},R=()=>u;this.init=f
```
### 34
```js
;for(let t in s)if(s[t].getActive())return!0;return!1},M=()=>{l&&l.clearRect(0,0,c.width,c.height)},P=()=>{if(!j()){l&&F();return}I(),M();for(let t in s)s[t].draw(l)},F=()=>{c.style.display!=`none`&&(c.style.display=`none`)},I=()=>{c.style.display!=`block`&&(c.style.display=`block`)},L=(t,a,s)=>{Engine.colorInterfaceNotificationManager.checkNotificationExist(t)&&Engine.colorInterfaceNotificationManager.updateData({action:r,id:t}),Engine.colorInterfaceNotificationManager.updateData({action:n,id:t,color:a,blur:s}),Engine.colorInterfaceNotificationManager.updateData({action:i,id:t})},R=()=>u;this.init=f,this.updateData=m,this.onC
```
### 35
```js
reateElement(`div`),this.timerWrapper.className=`c-timer c-timer--theme-${this.options.theme} ${this.options.cssClass}`,this.updateLowTimeClass(),this.progressBar=document.createElement(`div`),this.progressBar.className=`c-timer__progress-bar`,this.progressBar.style.width=`${this.timeRemaining/this.options.time*100}%`,this.textDisplay=document.createElement(`div`),this.textDisplay.className=`c-timer__text`,this.updateDisplay(),this.timerWrapper.appendChild(this.progressBar),this.timerWrapper.appendChild(this.textDisplay),this.options.tip&&(this.timerWrapper.title=this.options.tip),this.container&&this.container.appendChild(t
```
### 36
```js
(t);if(this.options.showMilliseconds&&n>0&&(r=`${t}.${Math.floor(n/100)}`),this.options.suffix&&(r+=`${this.options.suffix}`),this.textDisplay.textContent=r,this.progressBar){let t=this.options.time>0?this.timeRemaining/this.options.time*100:0;this.progressBar.style.width=`${Math.max(0,t)}%`}this.updateLowTimeClass()}start(){if(this.options.disabled){console.warn(`Timer is disabled`);return}this.timerId===null&&(this.timerId=setInterval(()=>{if(this.timeRemaining-=this.options.interval,this.timeRemaining<=0){this.timeRemaining=0,this.updateDisplay(),this.stop(),this.options.onFinish?.();return}this.updateDisplay(),this.optio
```
### 37
```js
eData[r])return;let i=this.storageData[r][n];i&&this.setIcon(t[0],i)}isDisabled(t){return t.classList.contains(`disabled`)}setIcon(t,n,r=!1){if(this.isDisabled(t))return;let i=t.querySelector(`.label`),a=i.querySelector(`.number`),s=i.querySelector(`.icons`);a.style.display=`none`,s.innerHTML=``,s.appendChild(this.getIcon(n)),s.style.display=`block`;let c=t.getAttribute(`data-tab-number`);if(r){let t=Engine.worldConfig.getWorldName();this.storageData[t][Number(c)]=n,this.setStorageData()}}setDefault(t,n){let r=t.querySelector(`.label`),i=r.querySelector(`.number`),a=r.querySelector(`.icons`);i.textContent=n,i.style.display=`bl
```
### 38
```js
isDisabled(t){return t.classList.contains(`disabled`)}setIcon(t,n,r=!1){if(this.isDisabled(t))return;let i=t.querySelector(`.label`),a=i.querySelector(`.number`),s=i.querySelector(`.icons`);a.style.display=`none`,s.innerHTML=``,s.appendChild(this.getIcon(n)),s.style.display=`block`;let c=t.getAttribute(`data-tab-number`);if(r){let t=Engine.worldConfig.getWorldName();this.storageData[t][Number(c)]=n,this.setStorageData()}}setDefault(t,n){let r=t.querySelector(`.label`),i=r.querySelector(`.number`),a=r.querySelector(`.icons`);i.textContent=n,i.style.display=`block`,a.style.display=`none`;let s=Engine.worldConfig.getWorldName();d
```
### 39
```js
c=t.getAttribute(`data-tab-number`);if(r){let t=Engine.worldConfig.getWorldName();this.storageData[t][Number(c)]=n,this.setStorageData()}}setDefault(t,n){let r=t.querySelector(`.label`),i=r.querySelector(`.number`),a=r.querySelector(`.icons`);i.textContent=n,i.style.display=`block`,a.style.display=`none`;let s=Engine.worldConfig.getWorldName();delete this.storageData[s][Number(n)],this.setStorageData()}getIcon(t,n=!1){let r=document.createElement(`div`);return r.classList.add(`ico`,`i-${t}`),n?r.outerHTML:r}};function DepoOpenTabs(){let t={fileName:`DepoOpenTabs.js`},n=null,r=!0,i=null,a=()=>{u()},s=t=>{r=t},c=()=>r,l=t=>t.id*
```
### 40
```js
ab-number`);if(r){let t=Engine.worldConfig.getWorldName();this.storageData[t][Number(c)]=n,this.setStorageData()}}setDefault(t,n){let r=t.querySelector(`.label`),i=r.querySelector(`.number`),a=r.querySelector(`.icons`);i.textContent=n,i.style.display=`block`,a.style.display=`none`;let s=Engine.worldConfig.getWorldName();delete this.storageData[s][Number(n)],this.setStorageData()}getIcon(t,n=!1){let r=document.createElement(`div`);return r.classList.add(`ico`,`i-${t}`),n?r.outerHTML:r}};function DepoOpenTabs(){let t={fileName:`DepoOpenTabs.js`},n=null,r=!0,i=null,a=()=>{u()},s=t=>{r=t},c=()=>r,l=t=>t.id*o$12.OPEN_TAB_AMOUNT-o$1
```
_Only first 40 of 81 matches shown._

## set-attribute-style
Matches: **0**


## css-text
Matches: **2**

### 1
```js
div`:`body`),i={visibility:`hidden`,width:0,height:0,border:0,margin:0,background:`none`},l&&t.extend(i,{position:`absolute`,left:`-1000px`,top:`-1000px`}),i)n.style[c]=i[c];n.appendChild(u),r=l||document.documentElement,r.insertBefore(n,r.firstChild),u.style.cssText=`position: absolute; left: 10.7432222px;`,a=t(u).offset().left,s=a>10&&11>a,n.innerHTML=``,r.removeChild(n)}()}(),t.ui.position,t.widget(`ui.draggable`,t.ui.mouse,{version:`1.11.1`,widgetEventPrefix:`drag`,options:{addClasses:!0,appendTo:`parent`,axis:!1,connectToSortable:!1,containment:!1,cursor:`auto`,cursorAt:!1,grid:!1,handle:!1,helper:`original`,iframe
```
### 2
```js
yte`},blue:{idx:2,type:`byte`}}},hsla:{props:{hue:{idx:0,type:`degrees`},saturation:{idx:1,type:`percent`},lightness:{idx:2,type:`percent`}}}},m={byte:{floor:!0,max:255},percent:{max:1},degrees:{mod:360,floor:!0}},h=f.support={},_=t(`<p>`)[0],v=t.each;_.style.cssText=`background-color:rgba(1,1,1,.5)`,h.rgba=_.style.backgroundColor.indexOf(`rgba`)>-1,v(p,function(t,n){n.cache=`_`+t,n.props.alpha={idx:3,type:`percent`,def:1}}),f.fn=t.extend(f.prototype,{parse:function(a,c,l,u){if(a===n)return this._rgba=[null,null,null,null],this;(a.jquery||a.nodeType)&&(a=t(a).css(c),c=n);var m=this,h=t.type(a),_=this._rgba=[];return c!=
```

## positioner
Matches: **113**

### 1
```js
ctStrings$1(BERSERK_GROUP,BERSERK_VARS.ELITE2);data.VARS.LOOT_FILTER.SOLO_BY_PRICE,data.VARS.LOOT_FILTER.SOLO_AUTO_ACCEPT,TEMPLATES[`border-window`]=`<div class="c-window border-window">     <!--<div class="border-image"></div>-->     <div class="header-label-positioner">         <div class="draggable-window-element"></div>         <div class="header-label">             <div class="left-decor"></div>             <div class="right-decor"></div>             <div class="text"></div>         </div>     </div>     <div class="content">         <!--<div class="decoration-label">-->             <!--<div class="decoration"></div>-
```
### 2
```js
iv>             <div class="stasis-overlay__time"></div>         </div>     </dev> </div>`,TEMPLATES[`map-reloader-splash`]=`<div class="map-reloader-splash map-overlay"></div>`,TEMPLATES[`dead-overlay`]=`<div class="dead-overlay map-overlay">     <div class="positioner">         <div class="inner-text" data-trans="unconcious_info_txt"></div>         <div class="dazed-time"></div>     </div> </div>`,TEMPLATES[`battle-bars-wrapper`]=`<div class="battle-bars-wrapper">     <div class="battle-bar energy" data-trans="data-tip#stat-energy">         <div class="background"></div>         <div class="bar-overflow">             <di
```
### 3
```js
  </div>             <!--<div class="bottom-wrapper"></div>-->         </div>         <div class="border"></div>         <div class="extended-stats scroll-wrapper small-bar">             <div class="border"></div>         </div>     </div>     <div class="top positioner">         <div class="bg"></div>         <div class="wanted-mini"></div>         <div class="content">             <div class="omg-tutorial-handler"></div>             <div class="character-bars-light-mode">               <div class="character-bars-tip-wrapper">                 <div class="hero-hp-top-progress-bar-light-mode interface-element-progress-bar-0
```
### 4
```js
class="top-left main-buttons-container"></div>             <div class="hud-container"></div>             <div class="matchmaking-timer"></div>             <div class="top-right main-buttons-container"></div>         </div>     </div>     <div class="under-top positioner">         <div class="bg"></div>         <div class="content">           <div class="under-top-left-widget-hamburger widget-hamburger">               <div class="icon hamburger-icon"></div>               <div class="amount interface-element-amount"></div>           </div>           <div class="under-top-right-widget-hamburger widget-hamburger">             
```
### 5
```js
          <div class="under-top-right-widget-hamburger widget-hamburger">               <div class="icon hamburger-icon"></div>               <div class="amount interface-element-amount"></div>           </div>         </div>     </div>     <div class="bottom positioner">         <div class="bg">         </div>         <div class="bg-additional-widget-left"></div>         <div class="bg-additional-widget-right"></div>         <div class="content">             <div class="bottom-left-additional main-buttons-container"></div>             <div class="bottom-right-additional main-buttons-container"></div>             <div clas
```
### 6
```js
div>     <div class="herocredits-difference"></div>     <div class="bm-register"></div> </div>`,TEMPLATES[`herogold-tip`]=`<div class="herogold-tip">     <div class="h-gold"></div>     <div class="h-gold-limit"></div> </div>`,TEMPLATES[`bottom-panel-of-bottom-positioner`]=`<div class="bottom-panel-of-bottom-positioner bottom-panel">     <div class="bottom-panel-graphic"></div>     <!--<div class="helpers-numbers">-->         <!--<span class="h-n-1">1</span>-->         <!--<span class="h-n-2">2</span>-->         <!--<span class="h-n-3">3</span>-->         <!--<span class="h-n-4">4</span>-->         <!--<span class="h-n-5">5
```
### 7
```js
v>     <div class="bm-register"></div> </div>`,TEMPLATES[`herogold-tip`]=`<div class="herogold-tip">     <div class="h-gold"></div>     <div class="h-gold-limit"></div> </div>`,TEMPLATES[`bottom-panel-of-bottom-positioner`]=`<div class="bottom-panel-of-bottom-positioner bottom-panel">     <div class="bottom-panel-graphic"></div>     <!--<div class="helpers-numbers">-->         <!--<span class="h-n-1">1</span>-->         <!--<span class="h-n-2">2</span>-->         <!--<span class="h-n-3">3</span>-->         <!--<span class="h-n-4">4</span>-->         <!--<span class="h-n-5">5</span>-->         <!--<span class="h-n-6">6</spa
```
### 8
```js
   <div class="news-time-promo-section">             <!--<div class="section-header" data-trans="#timePromo#news"></div>-->             <div class="section-content">                 <div class="time-promo-background"></div>                 <div class="package-positioner">                     <div class="package-wrapper"></div>                 </div>                 <div class="requires-text-wrapper">                     <div class="requires-text"></div>                 </div>             </div>         </div>      </div>     <div class="bottom-panel-graphics"></div> </div>`,TEMPLATES[`news-classic-tile`]=`<div class="news-
```
### 9
```js
 class="bottom-panel-graphics"></div> </div>`,TEMPLATES[`news-classic-tile`]=`<div class="news-classic-tile">     <div class="tile-background">         <div class="graphic-bck"></div>         <div class="title-bck"></div>     </div>     <div class="tile-items-positioner">         <div class="tile-items-wrapper"></div>     </div>     <div class="requires-text-wrapper">         <div class="requires-level"></div>         <div class="requires-text"></div>     </div>     <div class="used-text"></div>     <div class="buy-button-wrapper"></div>     <div class="buy-info"></div> </div>`,TEMPLATES[`news-time-promo-tile`]=`<div class
```
### 10
```js
lass="buy-info"></div> </div>`,TEMPLATES[`news-time-promo-tile`]=`<div class="news-time-promo-tile">     <div class="tile-background"></div>     <div class="title-time-promo-tile"></div>     <div class="price-time-promo-tile"></div>     <div class="tile-items-positioner">         <div class="tile-items-wrapper"></div>     </div>     <div class="used-text-wrapper">         <div class="used-text"></div>     </div>     <div class="buy-button-wrapper"></div>     <div class="buy-info"></div> </div>`,TEMPLATES[`buy-button-wrapper`]=`<div class="buy-button-wrapper buy-button"></div>`,TEMPLATES[`buy-button-news`]=`<div class="buy-
```
### 11
```js
mAlert(_t(`GoToMainPage`),[{txt:_t(`yes`),callback:function(){goToMainPage()}},{txt:_t(`no`),callback:function(){return!0}}])},window.goToMainPage=()=>{let t=getMainDomain();window.location.href=`https://margonem.${t}`},window.hideInterface=function(){$(`.top.positioner`).css(`display`,`none`),$(`.bottom.positioner`).css(`display`,`none`),$(`.right-column.main-column`).css(`display`,`none`),Engine.interface.get$gameLayer().css({top:`0px`,right:`0px`,bottom:`0px`})},window.getFreeIdOfObject=(t,n)=>{let r=isset$4(n)?n:0;for(;isset$4(t[r]);)r++;return r},window.getFreeIdOfArray=(t,n)=>{let r={};for(let n in t){let i=t[n].id;r
```
### 12
```js
back:function(){goToMainPage()}},{txt:_t(`no`),callback:function(){return!0}}])},window.goToMainPage=()=>{let t=getMainDomain();window.location.href=`https://margonem.${t}`},window.hideInterface=function(){$(`.top.positioner`).css(`display`,`none`),$(`.bottom.positioner`).css(`display`,`none`),$(`.right-column.main-column`).css(`display`,`none`),Engine.interface.get$gameLayer().css({top:`0px`,right:`0px`,bottom:`0px`})},window.getFreeIdOfObject=(t,n)=>{let r=isset$4(n)?n:0;for(;isset$4(t[r]);)r++;return r},window.getFreeIdOfArray=(t,n)=>{let r={};for(let n in t){let i=t[n].id;r[i]=!0}return getFreeIdOfObject(r,n)},window.g
```
### 13
```js
move;if(!u)return errorReport(n,r,`attr menuToAddAndRemove not exist`,t),!1;for(let i in u)if(!isset(u[i].id))return errorReport(n,r,`in element of menuToAddAndRemove not exist id attr`,t),!1;return!0}function j(){for(var r in h=Engine.interface.get$gameWindowPositioner().find(`.mAlert-layer`),i.addNewOption&&M(),t){let n=R(t[r]);f.push(n)}s.addClass(`menu-list`),T=$(`<div>`).addClass(`bck button small green no-hover`),T.append($(`<span>`).addClass(`menu-option`)),s.append(T),w=Templates_default.get(`dropdown-menu`),s.append(w),C=s.find(`.menu-arrow`),x=w,b=s.find(`.menu-wrapper`),y=s.find(`.wrapper`),u.capitalize||b.addCl
```
### 14
```js
(Character.prototype),Other.prototype.constructor=Other;function GroundItems(){var t=[],n=this,r=`/img/gui/item_frames/frames/item_frames.png`;let i=null,a=null;var s=0;this.init=function(){n.initFetch(),n.initDrop()};let c=t=>{let n=Engine.interface.getBottomPositioner().find(`.bottom-panel-of-bottom-positioner`),r={x:t.left,y:t.top},i=[[n.find(`.slots.right`),20],[n.find(`.slots.left`),20]];return checkPosIsCollisionWithLayers(r,i)};this.initDrop=function(){Engine.map.$worldPane.droppable({accept:`.item:not(.shop-item)`,drop:function(t,n){var r=n.draggable.data(`item`);if(Engine.trade||Engine.depo||Engine.shop||Engine.au
```
### 15
```js
ructor=Other;function GroundItems(){var t=[],n=this,r=`/img/gui/item_frames/frames/item_frames.png`;let i=null,a=null;var s=0;this.init=function(){n.initFetch(),n.initDrop()};let c=t=>{let n=Engine.interface.getBottomPositioner().find(`.bottom-panel-of-bottom-positioner`),r={x:t.left,y:t.top},i=[[n.find(`.slots.right`),20],[n.find(`.slots.left`),20]];return checkPosIsCollisionWithLayers(r,i)};this.initDrop=function(){Engine.map.$worldPane.droppable({accept:`.item:not(.shop-item)`,drop:function(t,n){var r=n.draggable.data(`item`);if(Engine.trade||Engine.depo||Engine.shop||Engine.auctions||Engine.mails||Engine.bonusReselectW
```
### 16
```js
f(n&&n.exp&&t.getLevel()){if(x!==null){var r=n.exp-x;r!==0&&t.showGainedExp(r,t.getLevel())}x=n.exp}},this.showGainedExp=function(t,n){let r=Engine.interface.get$interfaceLayer().find(`.gained-exp-indicator`),i=Engine.interface.get$interfaceLayer().find(`.top.positioner`).find(`.gained-exp-indicator-light-mode`);var a=Math.round(n**4+10),s=Math.round((n-1)**4+10);n==1&&(s=0);var c=t/(a-s),l=Math.round(c*1e4)/100,u=(t>0?`+`:`-`)+round(t)+` (`+Math.abs(l)+`%)`,f=(t>0?`+`:`-`)+round(t)+` (`+Math.abs(l)+`%)`;t>0?(r.css(`color`,`lime`),i.css(`color`,`lime`)):(r.css(`color`,`orangered`),i.css(`color`,`orangered`)),r.finish().tex
```
### 17
```js
n(n){t.tip(null),t.tipHide(n),r(null)},this.setMobileTipId=r,this.getMobileTipId=i}function Loader$1(){var t={},n=0;this.load=function(r){t[r]!=1&&(t[r]=!0,n+=20,this.updateProgressBar())},this.updateProgressBar=function(){var t=Engine.interface.get$gameWindowPositioner().find(`.loader-layer .progress-bar .inner`);setPercentProgressBar(t,n),n>=100&&Engine.interface.lock.unlock(`loader`)}}function DraconiteShop(){this.initWindow=function(){Engine.windowManager.add({content:Templates_default.get(`draconite-shop`),nameWindow:Engine.windowsData.name.DRACONITE_SHOP,nameRefInParent:`wnd`,objParent:this,resetBorderMargin:!0,twPad
```
### 18
```js
{name:EmotionsData_default.NAME.NPC_TALK,source_id:v.id,source_type:EmotionsData_default.OBJECT_TYPE.NPC}])}},this.clearTalkEmo=()=>{Engine.emotions.deleteEmoByType(EmotionsData_default.NAME.NPC_TALK)},this.useNormalDialog=function(){Engine.interface.getBottomPositioner().append(t.$),t.createNormalDialog(),t.setEmo(v.id),$(`.scroll-wrapper .scrollbar-wrapper`,t.$).length||($(`.npc-message-scroll`,t.$).addScrollBar({track:!0}),$(`.answers-scroll`,t.$).addScrollBar({track:!0}))},this.getBubble=function(){return n},this.checkNpcTalk=function(t,r,s){if(t&1){var c=_t(`end_talk1`,null,`talk`),l=Templates_default.get(`dialogue-wi
```
### 19
```js
State(t.myaccept,t.accept),this.buttonState(t.myaccept,t.accept)},this.init=function(){this.closeOtherWindows(),Engine.lock.add(`trade`),getEngine().interfaceItems.setDisableSlots(`trade`),this.$=Templates_default.get(`trade-window`),Engine.interface.getBottomPositioner().append(this.$),this.createTradeDialog(),this.createRightSide(),this.initButton(),this.initDropable(`show`,`s`),this.initDropable(`sell`,`t`),this.initGoldChange()},this.createTradeDialog=function(){var t=this.$.find(`.tip`),r=[`watch`,`show`,`buy`,`sell`,`gold-label`,`credits-label`];n.getDelayedNick(),t.tip(this.tLang(`how_trade_info`),`t_static`);for(va
```
### 20
```js
ss(`interface-element-active-card-background-stretch`)),c=$(`<div>`).addClass(`city-name`),l=$(`<div>`).addClass(`right-column-header`).append(c);r.find(`.right-scroll`).before(i,l);var u=$(`<div>`).addClass(`mini-map-wrapper`),f=$(`<div>`).addClass(`mini-map-positioner`);u.append(f),n.find(`.right-scroll .scroll-pane`).append(u);var p=$(`<div>`).addClass(`city-buffer-wrapper`),m=$(`<div>`).html(_t(`city_loading`)).addClass(`city-buffer`);p.append(m),r.append(p);var h=Templates_default.get(`button`).addClass(`set-tp-stone small green disable`);h.find(`.label`).html(_t(`set_tp`)),n.find(`.bottom-row-panel`).append(h),h.clic
```
### 21
```js
`);for(var a=0;a<n.length;a++){var s=n[a],c=Templates_default.get(`one-item-on-divide-list`).addClass(`cord-list-`+a);c.find(`.name`).html(s[0]+`, `+s[1]),c.data(`coords`,s),i.append(c),this.cordEvents(c,r,a)}},this.afterOnload=(r,a)=>{var s=n.find(`.mini-map-positioner`).empty();t.setMapBackground(a,r.width,r.height,s),i.push(a.name);for(var c=0;c<a.coords.length;c++){var l=a.coords[c],u=$(`<div>`).addClass(`cords cord-${c} map-${a.id}`).tip(l[0]+`, `+l[1]);s.append(u),t.setCords(u,l)}t.showHideBuffer(!1)},this.setMapBackground=function(r,i,a,s){var c={x:i/32,y:a/32};n.find(`.city-name`).html(r.name),t.setScale(c),s.css({
```
### 22
```js
X_1080]:{[IN_WINDOW]:standardWidgetSize,[TOP_LEFT]:standardWidgetSize,[TOP_RIGHT]:standardWidgetSize,[BOTTOM_LEFT]:standardWidgetSize,[BOTTOM_RIGHT]:standardWidgetSize,[BOTTOM_RIGHT_ADDITIONAL]:standardWidgetSize,[BOTTOM_LEFT_ADDITIONAL]:standardWidgetSize}}},PositionerData_default={TOP_POSITIONER:`TOP_POSITIONER`,UNDER_TOP_POSITIONER:`UNDER_TOP_POSITIONER`,BOTTOM_POSITIONER:`BOTTOM_POSITIONER`};function Interface(){var t=this;let n=422;var r=[];let i=null,a=!1,s=!1,c={},l=[],u=[],f=null,p=null,m,h,_,v,y,b,x,C,w,T,D,O,k,A,j,M,P,F,I=null,L=null,R=null,z=null,B=!1,V=null,H=241,U=t=>{B=t},G=()=>{let t=Engine.interface.get$int
```
### 23
```js
dWidgetSize,[TOP_LEFT]:standardWidgetSize,[TOP_RIGHT]:standardWidgetSize,[BOTTOM_LEFT]:standardWidgetSize,[BOTTOM_RIGHT]:standardWidgetSize,[BOTTOM_RIGHT_ADDITIONAL]:standardWidgetSize,[BOTTOM_LEFT_ADDITIONAL]:standardWidgetSize}}},PositionerData_default={TOP_POSITIONER:`TOP_POSITIONER`,UNDER_TOP_POSITIONER:`UNDER_TOP_POSITIONER`,BOTTOM_POSITIONER:`BOTTOM_POSITIONER`};function Interface(){var t=this;let n=422;var r=[];let i=null,a=!1,s=!1,c={},l=[],u=[],f=null,p=null,m,h,_,v,y,b,x,C,w,T,D,O,k,A,j,M,P,F,I=null,L=null,R=null,z=null,B=!1,V=null,H=241,U=t=>{B=t},G=()=>{let t=Engine.interface.get$interfaceLayer().find(`.stats-l
```
### 24
```js
_LEFT]:standardWidgetSize,[TOP_RIGHT]:standardWidgetSize,[BOTTOM_LEFT]:standardWidgetSize,[BOTTOM_RIGHT]:standardWidgetSize,[BOTTOM_RIGHT_ADDITIONAL]:standardWidgetSize,[BOTTOM_LEFT_ADDITIONAL]:standardWidgetSize}}},PositionerData_default={TOP_POSITIONER:`TOP_POSITIONER`,UNDER_TOP_POSITIONER:`UNDER_TOP_POSITIONER`,BOTTOM_POSITIONER:`BOTTOM_POSITIONER`};function Interface(){var t=this;let n=422;var r=[];let i=null,a=!1,s=!1,c={},l=[],u=[],f=null,p=null,m,h,_,v,y,b,x,C,w,T,D,O,k,A,j,M,P,F,I=null,L=null,R=null,z=null,B=!1,V=null,H=241,U=t=>{B=t},G=()=>{let t=Engine.interface.get$interfaceLayer().find(`.stats-light-mode`);R=ne
```
### 25
```js
ize,[TOP_RIGHT]:standardWidgetSize,[BOTTOM_LEFT]:standardWidgetSize,[BOTTOM_RIGHT]:standardWidgetSize,[BOTTOM_RIGHT_ADDITIONAL]:standardWidgetSize,[BOTTOM_LEFT_ADDITIONAL]:standardWidgetSize}}},PositionerData_default={TOP_POSITIONER:`TOP_POSITIONER`,UNDER_TOP_POSITIONER:`UNDER_TOP_POSITIONER`,BOTTOM_POSITIONER:`BOTTOM_POSITIONER`};function Interface(){var t=this;let n=422;var r=[];let i=null,a=!1,s=!1,c={},l=[],u=[],f=null,p=null,m,h,_,v,y,b,x,C,w,T,D,O,k,A,j,M,P,F,I=null,L=null,R=null,z=null,B=!1,V=null,H=241,U=t=>{B=t},G=()=>{let t=Engine.interface.get$interfaceLayer().find(`.stats-light-mode`);R=new CostComponent,z=new 
```
### 26
```js
rdWidgetSize,[BOTTOM_LEFT]:standardWidgetSize,[BOTTOM_RIGHT]:standardWidgetSize,[BOTTOM_RIGHT_ADDITIONAL]:standardWidgetSize,[BOTTOM_LEFT_ADDITIONAL]:standardWidgetSize}}},PositionerData_default={TOP_POSITIONER:`TOP_POSITIONER`,UNDER_TOP_POSITIONER:`UNDER_TOP_POSITIONER`,BOTTOM_POSITIONER:`BOTTOM_POSITIONER`};function Interface(){var t=this;let n=422;var r=[];let i=null,a=!1,s=!1,c={},l=[],u=[],f=null,p=null,m,h,_,v,y,b,x,C,w,T,D,O,k,A,j,M,P,F,I=null,L=null,R=null,z=null,B=!1,V=null,H=241,U=t=>{B=t},G=()=>{let t=Engine.interface.get$interfaceLayer().find(`.stats-light-mode`);R=new CostComponent,z=new CostComponent,R.init()
```
### 27
```js
M_LEFT]:standardWidgetSize,[BOTTOM_RIGHT]:standardWidgetSize,[BOTTOM_RIGHT_ADDITIONAL]:standardWidgetSize,[BOTTOM_LEFT_ADDITIONAL]:standardWidgetSize}}},PositionerData_default={TOP_POSITIONER:`TOP_POSITIONER`,UNDER_TOP_POSITIONER:`UNDER_TOP_POSITIONER`,BOTTOM_POSITIONER:`BOTTOM_POSITIONER`};function Interface(){var t=this;let n=422;var r=[];let i=null,a=!1,s=!1,c={},l=[],u=[],f=null,p=null,m,h,_,v,y,b,x,C,w,T,D,O,k,A,j,M,P,F,I=null,L=null,R=null,z=null,B=!1,V=null,H=241,U=t=>{B=t},G=()=>{let t=Engine.interface.get$interfaceLayer().find(`.stats-light-mode`);R=new CostComponent,z=new CostComponent,R.init(),z.init(),t.find(`.
```
### 28
```js
getSize,[BOTTOM_RIGHT]:standardWidgetSize,[BOTTOM_RIGHT_ADDITIONAL]:standardWidgetSize,[BOTTOM_LEFT_ADDITIONAL]:standardWidgetSize}}},PositionerData_default={TOP_POSITIONER:`TOP_POSITIONER`,UNDER_TOP_POSITIONER:`UNDER_TOP_POSITIONER`,BOTTOM_POSITIONER:`BOTTOM_POSITIONER`};function Interface(){var t=this;let n=422;var r=[];let i=null,a=!1,s=!1,c={},l=[],u=[],f=null,p=null,m,h,_,v,y,b,x,C,w,T,D,O,k,A,j,M,P,F,I=null,L=null,R=null,z=null,B=!1,V=null,H=241,U=t=>{B=t},G=()=>{let t=Engine.interface.get$interfaceLayer().find(`.stats-light-mode`);R=new CostComponent,z=new CostComponent,R.init(),z.init(),t.find(`.gold-currency`)[0].
```
### 29
```js
ages`,`crossStorage`,`charlist`],function(){let n=B;n||t.afterUnlock(),Engine.interfaceStart=!0,n||(devConsoleLog([`initialise onResize`]),Engine.onResize(),Engine.tutorialManager.startAfterInterfaceLoad())});let Y=()=>Engine.interfaceStart;this.get$gameWindowPositionerHeight=()=>f.height(),this.get$InterfaceLayerHeight=()=>this.get$interfaceLayer().height(),this.initPositioners=()=>{_=this.get$interfaceLayer().find(`.bottom.positioner`),v=this.get$interfaceLayer().find(`.top.positioner`),y=this.get$interfaceLayer().find(`.under-top.positioner`),b=f.find(`.right-column.main-column`)},this.get$rightColumn=()=>b,this.getBott
```
### 30
```js
Log([`initialise onResize`]),Engine.onResize(),Engine.tutorialManager.startAfterInterfaceLoad())});let Y=()=>Engine.interfaceStart;this.get$gameWindowPositionerHeight=()=>f.height(),this.get$InterfaceLayerHeight=()=>this.get$interfaceLayer().height(),this.initPositioners=()=>{_=this.get$interfaceLayer().find(`.bottom.positioner`),v=this.get$interfaceLayer().find(`.top.positioner`),y=this.get$interfaceLayer().find(`.under-top.positioner`),b=f.find(`.right-column.main-column`)},this.get$rightColumn=()=>b,this.getBottomPositioner=()=>_,this.getTopPositioner=()=>v,this.getUnderTopPositioner=()=>y,this.init$MAP_CANVAS=()=>{m=$(
```
### 31
```js
ialManager.startAfterInterfaceLoad())});let Y=()=>Engine.interfaceStart;this.get$gameWindowPositionerHeight=()=>f.height(),this.get$InterfaceLayerHeight=()=>this.get$interfaceLayer().height(),this.initPositioners=()=>{_=this.get$interfaceLayer().find(`.bottom.positioner`),v=this.get$interfaceLayer().find(`.top.positioner`),y=this.get$interfaceLayer().find(`.under-top.positioner`),b=f.find(`.right-column.main-column`)},this.get$rightColumn=()=>b,this.getBottomPositioner=()=>_,this.getTopPositioner=()=>v,this.getUnderTopPositioner=()=>y,this.init$MAP_CANVAS=()=>{m=$(`#MAP_CANVAS`)},this.init$GAME_CANVAS=()=>{h=$(`#GAME_CANVA
```
### 32
```js
gine.interfaceStart;this.get$gameWindowPositionerHeight=()=>f.height(),this.get$InterfaceLayerHeight=()=>this.get$interfaceLayer().height(),this.initPositioners=()=>{_=this.get$interfaceLayer().find(`.bottom.positioner`),v=this.get$interfaceLayer().find(`.top.positioner`),y=this.get$interfaceLayer().find(`.under-top.positioner`),b=f.find(`.right-column.main-column`)},this.get$rightColumn=()=>b,this.getBottomPositioner=()=>_,this.getTopPositioner=()=>v,this.getUnderTopPositioner=()=>y,this.init$MAP_CANVAS=()=>{m=$(`#MAP_CANVAS`)},this.init$GAME_CANVAS=()=>{h=$(`#GAME_CANVAS`)},this.init$gameWindowPositioner=()=>{f=$(`.game-
```
### 33
```js
=>f.height(),this.get$InterfaceLayerHeight=()=>this.get$interfaceLayer().height(),this.initPositioners=()=>{_=this.get$interfaceLayer().find(`.bottom.positioner`),v=this.get$interfaceLayer().find(`.top.positioner`),y=this.get$interfaceLayer().find(`.under-top.positioner`),b=f.find(`.right-column.main-column`)},this.get$rightColumn=()=>b,this.getBottomPositioner=()=>_,this.getTopPositioner=()=>v,this.getUnderTopPositioner=()=>y,this.init$MAP_CANVAS=()=>{m=$(`#MAP_CANVAS`)},this.init$GAME_CANVAS=()=>{h=$(`#GAME_CANVAS`)},this.init$gameWindowPositioner=()=>{f=$(`.game-window-positioner`)};let X=()=>{let t=t=>{let n=[[_t(`copy
```
### 34
```js
sitioners=()=>{_=this.get$interfaceLayer().find(`.bottom.positioner`),v=this.get$interfaceLayer().find(`.top.positioner`),y=this.get$interfaceLayer().find(`.under-top.positioner`),b=f.find(`.right-column.main-column`)},this.get$rightColumn=()=>b,this.getBottomPositioner=()=>_,this.getTopPositioner=()=>v,this.getUnderTopPositioner=()=>y,this.init$MAP_CANVAS=()=>{m=$(`#MAP_CANVAS`)},this.init$GAME_CANVAS=()=>{h=$(`#GAME_CANVAS`)},this.init$gameWindowPositioner=()=>{f=$(`.game-window-positioner`)};let X=()=>{let t=t=>{let n=[[_t(`copy-location-cords`),function(){copyClipboard(`${Engine.map.d.name} (${Engine.hero.getCords()})`
```
### 35
```js
terfaceLayer().find(`.bottom.positioner`),v=this.get$interfaceLayer().find(`.top.positioner`),y=this.get$interfaceLayer().find(`.under-top.positioner`),b=f.find(`.right-column.main-column`)},this.get$rightColumn=()=>b,this.getBottomPositioner=()=>_,this.getTopPositioner=()=>v,this.getUnderTopPositioner=()=>y,this.init$MAP_CANVAS=()=>{m=$(`#MAP_CANVAS`)},this.init$GAME_CANVAS=()=>{h=$(`#GAME_CANVAS`)},this.init$gameWindowPositioner=()=>{f=$(`.game-window-positioner`)};let X=()=>{let t=t=>{let n=[[_t(`copy-location-cords`),function(){copyClipboard(`${Engine.map.d.name} (${Engine.hero.getCords()})`)}],[_t(`copy-location`),fun
```
### 36
```js
tioner`),v=this.get$interfaceLayer().find(`.top.positioner`),y=this.get$interfaceLayer().find(`.under-top.positioner`),b=f.find(`.right-column.main-column`)},this.get$rightColumn=()=>b,this.getBottomPositioner=()=>_,this.getTopPositioner=()=>v,this.getUnderTopPositioner=()=>y,this.init$MAP_CANVAS=()=>{m=$(`#MAP_CANVAS`)},this.init$GAME_CANVAS=()=>{h=$(`#GAME_CANVAS`)},this.init$gameWindowPositioner=()=>{f=$(`.game-window-positioner`)};let X=()=>{let t=t=>{let n=[[_t(`copy-location-cords`),function(){copyClipboard(`${Engine.map.d.name} (${Engine.hero.getCords()})`)}],[_t(`copy-location`),function(){copyClipboard(`${Engine.m
```
### 37
```js
ight-column.main-column`)},this.get$rightColumn=()=>b,this.getBottomPositioner=()=>_,this.getTopPositioner=()=>v,this.getUnderTopPositioner=()=>y,this.init$MAP_CANVAS=()=>{m=$(`#MAP_CANVAS`)},this.init$GAME_CANVAS=()=>{h=$(`#GAME_CANVAS`)},this.init$gameWindowPositioner=()=>{f=$(`.game-window-positioner`)};let X=()=>{let t=t=>{let n=[[_t(`copy-location-cords`),function(){copyClipboard(`${Engine.map.d.name} (${Engine.hero.getCords()})`)}],[_t(`copy-location`),function(){copyClipboard(`${Engine.map.d.name}`)}],[_t(`copy-cords`),function(){copyClipboard(Engine.hero.getCords())}]];Engine.interface.showPopupMenu(n,getE(t))};w.o
```
### 38
```js
t$rightColumn=()=>b,this.getBottomPositioner=()=>_,this.getTopPositioner=()=>v,this.getUnderTopPositioner=()=>y,this.init$MAP_CANVAS=()=>{m=$(`#MAP_CANVAS`)},this.init$GAME_CANVAS=()=>{h=$(`#GAME_CANVAS`)},this.init$gameWindowPositioner=()=>{f=$(`.game-window-positioner`)};let X=()=>{let t=t=>{let n=[[_t(`copy-location-cords`),function(){copyClipboard(`${Engine.map.d.name} (${Engine.hero.getCords()})`)}],[_t(`copy-location`),function(){copyClipboard(`${Engine.map.d.name}`)}],[_t(`copy-cords`),function(){copyClipboard(Engine.hero.getCords())}]];Engine.interface.showPopupMenu(n,getE(t))};w.on(getRightClickEventName(),n=>t(n)
```
### 39
```js
t`,r=`show`;t?(w.addClass(n),D.addClass(n),A.addClass(r)):(w.removeClass(n),D.removeClass(n),A.removeClass(r))};this.interfaceFocus=!0,this.init=function(){at(function(n){t.interfaceFocus=!1}),it(function(n){t.interfaceFocus=!0}),ot(),st(),this.init$gameWindowPositioner(),this.blockWheel(),this.initCachedScripts(),this.initAppend(),this.initLayers(),Fe(),this.init$GAME_CANVAS(),this.initPositioners(),this.initMouseEvent(),mobileCheck()&&(getMobileMouse()||Oe(),Te()),this.initInterfaceTemplates(),this.createZoomOverlay(),this.heroElements=new HeroElements,this.heroElements.init(),this.mailsElements=new MailsElements(this),l
```
### 40
```js
s=!0,this.init=function(){at(function(n){t.interfaceFocus=!1}),it(function(n){t.interfaceFocus=!0}),ot(),st(),this.init$gameWindowPositioner(),this.blockWheel(),this.initCachedScripts(),this.initAppend(),this.initLayers(),Fe(),this.init$GAME_CANVAS(),this.initPositioners(),this.initMouseEvent(),mobileCheck()&&(getMobileMouse()||Oe(),Te()),this.initInterfaceTemplates(),this.createZoomOverlay(),this.heroElements=new HeroElements,this.heroElements.init(),this.mailsElements=new MailsElements(this),le(),ue(),ee(),te(),Q(),ne(),re(),X(),de(),se(),ce(),G(),xe();var n=this.get$loaderLayer().find(`.progress-bar .inner`);n.css(`disp
```
_Only first 40 of 113 matches shown._

## game-window-positioner
Matches: **3**

### 1
```js
n`)},this.get$rightColumn=()=>b,this.getBottomPositioner=()=>_,this.getTopPositioner=()=>v,this.getUnderTopPositioner=()=>y,this.init$MAP_CANVAS=()=>{m=$(`#MAP_CANVAS`)},this.init$GAME_CANVAS=()=>{h=$(`#GAME_CANVAS`)},this.init$gameWindowPositioner=()=>{f=$(`.game-window-positioner`)};let X=()=>{let t=t=>{let n=[[_t(`copy-location-cords`),function(){copyClipboard(`${Engine.map.d.name} (${Engine.hero.getCords()})`)}],[_t(`copy-location`),function(){copyClipboard(`${Engine.map.d.name}`)}],[_t(`copy-cords`),function(){copyClipboard(Engine.hero.getCords())}]];Engine.interface.showPopupMenu(n,getE(t))};w.on(getRightClickEventName(),n=>t(n)
```
### 2
```js
eturn;let r=n.getWidget();Je(r,t,!0),getEngine().hotKeys.replaceMatchmakingTipNames()},$e=t=>{let n=this.getAttachWidgetByName(t);n&&et(n,t)};this.addDraggableAndDataAndTip=(n,r,i,a,s={})=>{let c={helper:`clone`,distance:5,cursorAt:{top:16,left:16},appendTo:`.game-window-positioner`,scroll:!1,zIndex:20,start:function(t,n){startDraggingEvent($(this)),console.log(`start`)},stop:function(t,n){stopDraggingEvent($(this)),console.log(`stop`)}};if(s.tipText?n.tip(s.tipText):Je(n,i,s.permission),a){elementIsObject(a)||(errorReport(t.fileName,`addDraggableAndDataAndTip`,`incorrect format of options`,a),a={});for(let t in a)c[t]=a[t]}n.data(r,i
```
### 3
```js
loc:`g`,tpl:25364}},[ProfData_default.TRACKER]:{24:{loc:`g`,tpl:25364}},[ProfData_default.HUNTER]:{24:{loc:`g`,tpl:25364}},[ProfData_default.BLADE_DANCER]:{24:{loc:`g`,tpl:25364}}},minOneOfAllNotEquip:!0},graphic:`/img/gui/newTutorial/12.gif`,htmlMultiGlow:[`.game-window-positioner>.interface-layer>.right-column>.inner-wrapper>.inventory_wrapper>.bags-navigation>.tutorial-bag`],htmlPosition:`.interface-layer>.right-column.main-column`,minLevel:10,maxLevel:20,idMaps:[707],blink:!0,blockedWidget:[i],blockedHotKeys:[n],additionalFunctionBeforeCreate:t.manageEqColumn}],34:[{textPc:`t_34_ni_pl`,textMobile:`t_34_ni_mobile_pl`,headerPc:`t_he
```

## hud-container
Matches: **8**

### 1
```js
get-hamburger">                 <div class="icon hamburger-icon"></div>                 <div class="amount interface-element-amount"></div>             </div>                          <div class="top-left main-buttons-container"></div>             <div class="hud-container"></div>             <div class="matchmaking-timer"></div>             <div class="top-right main-buttons-container"></div>         </div>     </div>     <div class="under-top positioner">         <div class="bg"></div>         <div class="content">           <div class="under-top-left-widget-hamburger widget-hamburger">               <div class="icon hambur
```
### 2
```js
ain-buttons-container"></div>             <div class="bottom-right main-buttons-container">                 <div class="version-info"></div>                 <div class="game-notifications"></div>             </div>         </div>     </div> </div>`,TEMPLATES[`hud-container`]=`<div class="hud-container">     <div class="btn-min gold-btn">+</div>     <div class="btn-min credits-btn">+</div>     <div class="map_ball"></div>     <div class="hero-data">         <span class="heroname"></span>     </div>     <div class="map-data">         <span class="map-timer"></span>         <span class="location-id"></span>         <span class="
```
### 3
```js
             <div class="bottom-right main-buttons-container">                 <div class="version-info"></div>                 <div class="game-notifications"></div>             </div>         </div>     </div> </div>`,TEMPLATES[`hud-container`]=`<div class="hud-container">     <div class="btn-min gold-btn">+</div>     <div class="btn-min credits-btn">+</div>     <div class="map_ball"></div>     <div class="hero-data">         <span class="heroname"></span>     </div>     <div class="map-data">         <span class="map-timer"></span>         <span class="location-id"></span>         <span class="location"></span>         <sp
```
### 4
```js
s_default.get(`hp-indicator-wrapper`),n=Templates_default.get(`exp-bar-wrapper`),r=Templates_default.get(`battle-bars-wrapper`),i=Templates_default.get(`extended-stats-tpl`),a=Templates_default.get(`bottom-panel-of-bottom-positioner`),s=Templates_default.get(`hud-container`);let c=this.get$interfaceLayer();c.find(`.bottom.positioner .content`).append(a),c.find(`.hp-indicator-wrapper-template`).append(t),c.find(`.hud-container`).replaceWith(s),c.find(`.exp-bar-wrapper-template`).append(n),c.find(`.battle-bars-wrapper-template`).append(r),c.find(`.extended-stats`).append(i),p.append(Templates_default.get(`stasis-incoming-overla
```
### 5
```js
ended-stats-tpl`),a=Templates_default.get(`bottom-panel-of-bottom-positioner`),s=Templates_default.get(`hud-container`);let c=this.get$interfaceLayer();c.find(`.bottom.positioner .content`).append(a),c.find(`.hp-indicator-wrapper-template`).append(t),c.find(`.hud-container`).replaceWith(s),c.find(`.exp-bar-wrapper-template`).append(n),c.find(`.battle-bars-wrapper-template`).append(r),c.find(`.extended-stats`).append(i),p.append(Templates_default.get(`stasis-incoming-overlay`)),p.append(Templates_default.get(`stasis-overlay`)),p.append(Templates_default.get(`map-reloader-splash`)),p.append(Templates_default.get(`dead-overlay`)
```
### 6
```js
	    .dialogue-window { 			        bottom: 81px; 			    } 			    .interface-layer .battle-controller.with-skills { 			        bottom: 50px; 			    } 			    .interface-layer .mini-map-controller { 			        top:50px; 			        bottom: 50px; 			    }  			    .hud-container, 			    .bottom-panel-of-bottom-positioner.bottom-panel { 			        transform: scale(0.82); 			    } 			    .hud-container { 	                -webkit-transform-origin-y: 10%;                 }                 .bottom-panel-of-bottom-positioner.bottom-panel { 	                transform-origin: 50% 100%;                 }                 .interface-layer .to
```
### 7
```js
  bottom: 50px; 			    } 			    .interface-layer .mini-map-controller { 			        top:50px; 			        bottom: 50px; 			    }  			    .hud-container, 			    .bottom-panel-of-bottom-positioner.bottom-panel { 			        transform: scale(0.82); 			    } 			    .hud-container { 	                -webkit-transform-origin-y: 10%;                 }                 .bottom-panel-of-bottom-positioner.bottom-panel { 	                transform-origin: 50% 100%;                 }                 .interface-layer .top.positioner .bg {                     background-position-y: -71px!important;                 }                 .bottom-lef
```
### 8
```js
.bg-additional-widget-right {                     transform: scale(1, 0.82);                     transform-origin: 0% -5%;                 }              }              body[data-res="${n._1024_X_768}"],             body[data-res="${n._1173_X_555}"] { 			    .hud-container, 			    .bottom-panel-of-bottom-positioner.bottom-panel { 			        transform: scale(0.9); 			    } 			}  		</style> 	`}}var addonsScripts={addon_1:_1,addon_3:_3,addon_7:_7,addon_8:_8,addon_11:_11,addon_19:_19,addon_21:_21,addon_24:_24,addon_25:_25,addon_27:_27,addon_28:_28};addonsScripts.addon_17&&(errorReport$1(`AddonsPanel.js`,`AddonsPanel.js`,`In past 
```

## bottom-panel
Matches: **67**

### 1
```js
 class="herocredits"></div>     <div class="herocredits-difference"></div>     <div class="bm-register"></div> </div>`,TEMPLATES[`herogold-tip`]=`<div class="herogold-tip">     <div class="h-gold"></div>     <div class="h-gold-limit"></div> </div>`,TEMPLATES[`bottom-panel-of-bottom-positioner`]=`<div class="bottom-panel-of-bottom-positioner bottom-panel">     <div class="bottom-panel-graphic"></div>     <!--<div class="helpers-numbers">-->         <!--<span class="h-n-1">1</span>-->         <!--<span class="h-n-2">2</span>-->         <!--<span class="h-n-3">3</span>-->         <!--<span class="h-n-4">4</span>-->         <!--
```
### 2
```js
redits-difference"></div>     <div class="bm-register"></div> </div>`,TEMPLATES[`herogold-tip`]=`<div class="herogold-tip">     <div class="h-gold"></div>     <div class="h-gold-limit"></div> </div>`,TEMPLATES[`bottom-panel-of-bottom-positioner`]=`<div class="bottom-panel-of-bottom-positioner bottom-panel">     <div class="bottom-panel-graphic"></div>     <!--<div class="helpers-numbers">-->         <!--<span class="h-n-1">1</span>-->         <!--<span class="h-n-2">2</span>-->         <!--<span class="h-n-3">3</span>-->         <!--<span class="h-n-4">4</span>-->         <!--<span class="h-n-5">5</span>-->         <!--<span
```
### 3
```js
 class="bm-register"></div> </div>`,TEMPLATES[`herogold-tip`]=`<div class="herogold-tip">     <div class="h-gold"></div>     <div class="h-gold-limit"></div> </div>`,TEMPLATES[`bottom-panel-of-bottom-positioner`]=`<div class="bottom-panel-of-bottom-positioner bottom-panel">     <div class="bottom-panel-graphic"></div>     <!--<div class="helpers-numbers">-->         <!--<span class="h-n-1">1</span>-->         <!--<span class="h-n-2">2</span>-->         <!--<span class="h-n-3">3</span>-->         <!--<span class="h-n-4">4</span>-->         <!--<span class="h-n-5">5</span>-->         <!--<span class="h-n-6">6</span>-->        
```
### 4
```js
iv>`,TEMPLATES[`herogold-tip`]=`<div class="herogold-tip">     <div class="h-gold"></div>     <div class="h-gold-limit"></div> </div>`,TEMPLATES[`bottom-panel-of-bottom-positioner`]=`<div class="bottom-panel-of-bottom-positioner bottom-panel">     <div class="bottom-panel-graphic"></div>     <!--<div class="helpers-numbers">-->         <!--<span class="h-n-1">1</span>-->         <!--<span class="h-n-2">2</span>-->         <!--<span class="h-n-3">3</span>-->         <!--<span class="h-n-4">4</span>-->         <!--<span class="h-n-5">5</span>-->         <!--<span class="h-n-6">6</span>-->         <!--<span class="h-n-7">7</spa
```
### 5
```js
       <div class="usable-slot usable-slot-4 interface-element-one-item-slot-2" data-slot-index="4"></div>     </div>     <div class="exp-bar-wrapper-template"></div>     <div class="exp-bar"></div>     <div class="gained-exp-indicator"></div>     <div class="bottom-panel-pointer-bg">         <div class="pointer-exp-graphic"></div>         <div class="pointer-ttl-graphic"></div>         <div class="pointer-exp" data-trans="data-tip#exp#exp-ttl-pointer"></div>         <div class="pointer-ttl" data-trans="data-tip#ttl#exp-ttl-pointer"></div>     </div>     <div class="skill-usable-slots left">         <div class="skill-usable-
```
### 6
```js
ole-content></div>         </div>     </div>     <div class="input-wrapper">         <div class="gt_console">&gt;</div>         <input class="console-input" id="console_input" placeholder="Console input" autocomplete="off"/>     </div>     <div class="console-bottom-panel-wrapper">         <!--<div class="console-bottom-panel"></div>-->         <div class="interface-element-bottom-bar-background-stretch"></div>     </div> </div>`,TEMPLATES[`console-message`]=`<div class="console-message"></div>`,TEMPLATES[`wanted-list`]=`<div class="wanted-list">     <div class="scroll-wrapper small-bar">         <div class="scroll-pane">   
```
### 7
```js
lass="input-wrapper">         <div class="gt_console">&gt;</div>         <input class="console-input" id="console_input" placeholder="Console input" autocomplete="off"/>     </div>     <div class="console-bottom-panel-wrapper">         <!--<div class="console-bottom-panel"></div>-->         <div class="interface-element-bottom-bar-background-stretch"></div>     </div> </div>`,TEMPLATES[`console-message`]=`<div class="console-message"></div>`,TEMPLATES[`wanted-list`]=`<div class="wanted-list">     <div class="scroll-wrapper small-bar">         <div class="scroll-pane">             <div class="empty row-in-trans-window">----</
```
### 8
```js
aner"></div>`,TEMPLATES[`mails-window`]=` <div class="mails-window">     <div class="how-mail-or-char"></div>     <div class="mails-window__tabs"></div>     <div class="mails-window__contents"></div>     <div class="bottom-mail-panel">         <!--<div class="bottom-panel-graphics"></div>-->         <div class="interface-element-bottom-bar-background-stretch"></div>     </div> </div>`,TEMPLATES[`mail-column`]=`<div class="mail-column">     <div class="middle-graphic interface-element-middle-1-background"></div>     <div class="content-header interface-element-bottom-bar-background-stretch"></div>     <div class="scroll-wrapp
```
### 9
```js
          <div class="package-wrapper"></div>                 </div>                 <div class="requires-text-wrapper">                     <div class="requires-text"></div>                 </div>             </div>         </div>      </div>     <div class="bottom-panel-graphics"></div> </div>`,TEMPLATES[`news-classic-tile`]=`<div class="news-classic-tile">     <div class="tile-background">         <div class="graphic-bck"></div>         <div class="title-bck"></div>     </div>     <div class="tile-items-positioner">         <div class="tile-items-wrapper"></div>     </div>     <div class="requires-text-wrapper">         <
```
### 10
```js
      <div class="right-scroll scroll-wrapper classic-bar">             <div class="scroll-pane"></div>         </div>     </div>     <div class="bottom-part">         <div class="interface-element-bottom-bar-background-stretch"></div>         <!--<div class="bottom-panel-graphics"></div>-->     </div> </div>`,TEMPLATES.table=`     <table class="table">         <thead></thead>         <tbody></tbody>     </table> `,TEMPLATES[`table-component`]=`     <div class="c-table"></div> `,TEMPLATES[`table-wrapper`]=`     <div class="table__wrapper">         <table class="table__header"></table>     </div> `,TEMPLATES[`table-scrollbar`
```
### 11
```js
s="scroll-pane">                         <table class="auction-table interface-element-table-3"></table>                     </div>                 </div>             </div>         </div>                  <div class="bottom-part">             <!--<div class="bottom-panel-graphics"></div>-->             <div class="interface-element-bottom-bar-background-stretch"></div> <!--                <div class="additional-soulbond-payment" data-trans="#filter_bound_price_info#auction"></div>-->             <div class="auction-off-btn-wrapper"></div>             <div class="auction-renew-btn-wrapper"></div>             <div class="amou
```
### 12
```js
                <div class="empty-reset-button"></div>                     </div>                 </div>                 <div class="description-wrapper"></div>             </div>         </div>     </div>     <div class="bottom-part">         <!--<div class="bottom-panel-graphics"></div>-->         <div class="interface-element-bottom-bar-background-stretch"></div>         <div class="free-skills-label"></div>         <div class="MB-wrapper">             <div class="MB-label-1" data-trans="#available_label"></div>             <div class="info-icon" data-trans="data-tip#mb_tip"></div>             <div class="MB-label-2" data
```
### 13
```js
div class="premium-label" data-trans="#premium_rewards"></div>                 </div>             </div>         </div>     </div>     <div class="bottom-row-panel">     <div class="interface-element-middle-2-background-stretch"></div>         <!--<div class="bottom-panel-graphics"></div>-->         <div class="your-all-points-wrapper">             <div class="all-points-icon"></div>             <div class="points"></div>         </div>     </div>   </div>`,TEMPLATES[`battle-pass-mission-tile`]=`<div class="battle-pass-mission-tile">      <div class="mission-reward-wrapper">         <div class="mission-reward-icon"></div>   
```
### 14
```js
  <div class="outfit-header interface-element-table-header-1-background"></div>         <div class="outfit-wrapper">             <div class="outfit-graphic"></div>         </div>     </div>      <div class="bottom-change-outfit-panel">         <!--<div class="bottom-panel-graphics"></div>-->         <div class="interface-element-bottom-bar-background-stretch"></div>         <div class="save-button"></div>     </div> </div>`,TEMPLATES[`character-reset`]=`<div class="character-reset">     <div class="graphic-background interface-element-middle-1-background"></div>     <div class="sex-section">         <div class="info-box" dat
```
### 15
```js
chmaking"></div>         <div class="classification-match wood-bar">             <div class="interface-element-header-1-background-stretch"></div>             <div class="classification-match-val wood-bar-val"></div>         </div>     </div>      <div class="bottom-panel-graphics">     <div class="interface-element-bottom-bar-background-stretch"></div>         <div class="tokens-amount"></div>         <div class="close-wrapper"></div>     </div> </div>`,TEMPLATES.card=`<div class="card">     <div class="label">         <div class="number"></div>         <div class="icons">             <div class="cl-icon icon-soulbound"></d
```
### 16
```js
 class="cards-header"></div>     </div>     <div class="scroll-wrapper classic-bar">         <div class="scroll-pane">             <div class="middle-graphics interface-element-middle-1-background">             </div>         </div>     </div>     <div class="bottom-panel-graphics">         <div class="interface-element-bottom-bar-background-stretch"></div>     </div> </div>`,TEMPLATES[`one-achievement`]=`<div class="one-achievement">     <div class="title-wrapper">         <div class="achievement-title"></div>         <div class="state-wrapper">             <span>[</span>             <span class="current"></span>           
```
### 17
```js
anel`]=`<div class="matchmaking-panel">     <div class="header-wrapper">         <div class="graphic"></div>         <div class="edit-header-label"></div>     </div>     <div class="middle-graphics interface-element-middle-1-background"></div>     <div class="bottom-panel-graphics">         <div class="interface-element-bottom-bar-background-stretch"></div>     </div>     <div class="all-pages">         <div class="matchmaking-menu main-wnd">             <div class="show-reward-season-item"></div>             <div class="matchmaking-menu-bottom-panel">                 <div class="turn-on-off-tutorial"></div>                 
```
### 18
```js
        <div class="interface-element-bottom-bar-background-stretch"></div>     </div>     <div class="all-pages">         <div class="matchmaking-menu main-wnd">             <div class="show-reward-season-item"></div>             <div class="matchmaking-menu-bottom-panel">                 <div class="turn-on-off-tutorial"></div>                 <div class="warning-points" data-trans="data-tip#warning_point_desc">                     <div class="info-icon"></div>                     <div class="text"></div>                 </div>             </div>         </div>          <div class="choose-eq main-wnd no-exit">             
```
### 19
```js
</div>             </div>         </div>          <div class="choose-eq main-wnd no-exit">             <div class="builds-wrapper scroll-wrapper classic-bar">                 <div class="scroll-pane"></div>             </div>             <div class="choose-eq-bottom-panel">                 <div class="time-ball">                     <div class="time">10 s</div>                 </div>                 <div class="blink-wait-label" data-trans="#wait-for-label#matchmaking"></div>                 <div class="you-info">                     <div class="avatar-wrapper">                         <div class="avatar-icon"></div>        
```
### 20
```js
-wrapper">                         <div class="details-btn"></div>                         <div class="go-to-shop-btn"></div>                     </div>                 </div>                 <div class="right-side"></div>                 <div class="progress-bottom-panel">                     <div class="chempions-amount"></div>                     <div class="back-to-main"></div>                     <div class="get-all"></div>                 </div>             </div>             <div class="stats-wnd section">                 <div class="scroll-wrapper classic-bar scrollable">                     <div class="scroll-pane">
```
### 21
```js
>                 <div class="scroll-wrapper classic-bar scrollable">                     <div class="scroll-pane">                         <table class="stats-table"></table>                     </div>                 </div>                 <div class="stats-bottom-panel">                     <div class="back-to-main"></div>                     <div class="stats-info" data-trans="#statisticsinfo_tip#matchmaking"></div>                 </div>             </div>              <div class="history-wnd section">                 <table class="history-table"></table>                 <div class="history-bottom-panel">               
```
### 22
```js
     <div class="stats-info" data-trans="#statisticsinfo_tip#matchmaking"></div>                 </div>             </div>              <div class="history-wnd section">                 <table class="history-table"></table>                 <div class="history-bottom-panel">                     <div class="back-to-main"></div>                     <div class="page-info"></div>                     <div class="prev-page"></div>                     <div class="input-wrapper"></div>                     <div class="next-page"></div>                 </div>             </div>              <div class="season-wnd section">             
```
### 23
```js
s="players-in-ranking-info"></div>                         <div class="amount-players-got-outfit-info"></div>                         <div class="wrapper-outfit-info"></div>                     </div>                 </div>                  <div class="season-bottom-panel">                     <!--<div class="season-tip-info info-icon" data-trans="data-tip#rankingpoints#matchmaking"></div>-->                     <!--<div class="played-battle"></div>-->                     <div class="back-to-main"></div>                     <div class="your-records">                         <div class="your-season-record"></div>             
```
### 24
```js
           </div>                     </div>                 </div>             </div>              <div class="statistics-detailed-wnd section">                 <table class="statistics-detailed-table"></table>                 <div class="statistics-detailed-bottom-panel">                     <div class="back-to-main"></div>                 </div>             </div>         </div>          <div class="matchmaking-ranking main-wnd">             <div class="ranking-tabs"></div>             <div class="general-ranking-wnd section">                 <table class="ranking-table"></table>                 <div class="ladder_global-
```
### 25
```js
      </div>          <div class="matchmaking-ranking main-wnd">             <div class="ranking-tabs"></div>             <div class="general-ranking-wnd section">                 <table class="ranking-table"></table>                 <div class="ladder_global-bottom-panel ranking-bottom-panel">                     <div class="refresh"></div>                     <div class="back-to-main"></div>                     <div class="page-info"></div>                     <div class="prev-page"></div>                     <div class="input-wrapper"></div>                     <div class="next-page"></div>                 </div>         
```
### 26
```js
 <div class="matchmaking-ranking main-wnd">             <div class="ranking-tabs"></div>             <div class="general-ranking-wnd section">                 <table class="ranking-table"></table>                 <div class="ladder_global-bottom-panel ranking-bottom-panel">                     <div class="refresh"></div>                     <div class="back-to-main"></div>                     <div class="page-info"></div>                     <div class="prev-page"></div>                     <div class="input-wrapper"></div>                     <div class="next-page"></div>                 </div>             </div>           
```
### 27
```js
              </div>             </div>             <div class="clan-ranking-wnd section">                 <table class="ranking-table"></table>                 <div class="text-info" data-trans="#clan_not_exist"></div>                 <div class="ladder_clan-bottom-panel ranking-bottom-panel">                     <div class="refresh"></div>                     <div class="back-to-main"></div>                     <div class="page-info"></div>                     <div class="prev-page"></div>                     <div class="input-wrapper"></div>                     <div class="next-page"></div>                 </div>         
```
### 28
```js
            </div>             <div class="clan-ranking-wnd section">                 <table class="ranking-table"></table>                 <div class="text-info" data-trans="#clan_not_exist"></div>                 <div class="ladder_clan-bottom-panel ranking-bottom-panel">                     <div class="refresh"></div>                     <div class="back-to-main"></div>                     <div class="page-info"></div>                     <div class="prev-page"></div>                     <div class="input-wrapper"></div>                     <div class="next-page"></div>                 </div>             </div>           
```
### 29
```js
      </div>             </div>             <div class="friends-ranking-wnd section">                 <table class="ranking-table"></table>                 <div class="text-info" data-trans="#friend_not_exist"></div>                 <div class="ladder_friends-bottom-panel ranking-bottom-panel">                     <div class="refresh"></div>                     <div class="back-to-main"></div>                     <div class="page-info"></div>                     <div class="prev-page"></div>                     <div class="input-wrapper"></div>                     <div class="next-page"></div>                 </div>         
```
### 30
```js
    </div>             <div class="friends-ranking-wnd section">                 <table class="ranking-table"></table>                 <div class="text-info" data-trans="#friend_not_exist"></div>                 <div class="ladder_friends-bottom-panel ranking-bottom-panel">                     <div class="refresh"></div>                     <div class="back-to-main"></div>                     <div class="page-info"></div>                     <div class="prev-page"></div>                     <div class="input-wrapper"></div>                     <div class="next-page"></div>                 </div>             </div>         </
```
### 31
```js
nfo-2 txt-info" data-trans="#txt-info-2#matchmaking"></div>             <div class="your-reward-wrapper">                 <div class="your-reward"></div>                 <div class="your-outfits"></div>             </div>             <div class="season-reward-bottom-panel">                 <div class="take-reward"></div>                 <div class="take-reward-now"></div>             </div>         </div>      </div>     <!--<div class="time-ball">-->     <!--<div class="time"></div>-->     <!--</div>--> </div>`,TEMPLATES[`fight-result`]=`<div class="fight-result"></div>`,TEMPLATES[`season-outfit`]=`<div class="season-outfit
```
### 32
```js
/div>-->         <div class="left-scroll scroll-wrapper classic-bar">             <div class="scroll-pane">                 <div class="items-list"></div>             </div>         </div>     </div>      <div class="bottom-row-panel">         <!--<div class="bottom-panel-graphics"></div>-->         <div class="interface-element-bottom-bar-background-stretch"></div>         <div class="filter-label" data-trans="#filter-level"></div>         <div class="start-lvl-wrapper"></div>         <div class="stop-lvl-wrapper"></div>         <div class="choose-prof-wrapper">             <div class="choose-prof menu"></div>         </div
```
### 33
```js
(),this.initContent(),this.initInputKeyCodes(),this.initScrollBar(),this.initSizeButton()};let c=()=>{if(a)return;let n=createButton(`CSS_THEME`,[`small`,`css-theme-button`],function(){getEngine().cssLoader.createWindow(),t.close()});this.wnd.$.find(`.console-bottom-panel-wrapper`)[0].appendChild(n),a=!0},l=()=>{let t=Engine&&Engine.interface&&Engine.interface.getStateOfLightInterfaceFromStorage();return t=t||t==null,t?_t(`off`,null,`buttons`)+` `+_t(`TEST_APP`):_t(`on`,null,`buttons`)+` `+_t(`TEST_APP`)},u=()=>{if(!isMobileApp()||s)return;let t=l(),n=createButton(t,[`small`,`green`,`mobile-test`],function(){let n=Engine.int
```
### 34
```js
 t=l(),n=createButton(t,[`small`,`green`,`mobile-test`],function(){let n=Engine.interface;if(n.toggleInterfaceLightMode(),t=l(),$(this).find(`.label`).html(t),n.getInterfaceLightMode()){var r=n.findTheBestZoom();n.setZoomFactor(r)}});this.wnd.$.find(`.console-bottom-panel-wrapper`)[0].appendChild(n),s=!0},f=()=>{if(!mobileCheck()||i)return;let n=createButton(`PREV_CMD`,[`small`,`prev-cmd-button`],function(){t.commandLine.previous()}),r=createButton(`NEXT_CMD`,[`small`,`next-cmd-button`],function(){t.commandLine.next()}),a=this.wnd.$.find(`.console-bottom-panel-wrapper`)[0];a.appendChild(n),a.appendChild(r),i=!0};this.initSiz
```
### 35
```js
ild(n),s=!0},f=()=>{if(!mobileCheck()||i)return;let n=createButton(`PREV_CMD`,[`small`,`prev-cmd-button`],function(){t.commandLine.previous()}),r=createButton(`NEXT_CMD`,[`small`,`next-cmd-button`],function(){t.commandLine.next()}),a=this.wnd.$.find(`.console-bottom-panel-wrapper`)[0];a.appendChild(n),a.appendChild(r),i=!0};this.initSizeButton=function(){this.wnd.$.find(`.console-window`).find(`.size-button`).on(getClickEventName(),function(){t.wnd.$.find(`.console-window`).toggleClass(`big-size`),$(`.scroll-wrapper`,t.wnd.$).trigger(`update`),t.wnd.center()})},this.setVisibleOnSizeButton=function(){this.wnd.$.find(`.console
```
### 36
```js
(`button`);r.addClass(`global-addons-exist`),i.addClass(`small green global-addons-state-button`),i.find(`.label`).text(t?_t(`global-addons-off`):_t(`global-addons-on`)),i.css(`display`,`none`),n&&i.addClass(n),i.click(()=>{s(),pageReload()}),r.find(`.console-bottom-panel-wrapper`).append(i)},f=t=>{let n=Engine.console.wnd.$,r=t?`block`:`none`;n.find(`.global-addons-state-button`).css(`display`,r)},p=n=>{t=n,c()};this.init=n,this.initGlobalAddonLink=r,this.checkAddonsTurnOn=a,this.checkIsGlobalAddonRequestAnswer=i,this.setMsgInConsoleAndCreateButtonInConsole=l,this.setVisibleOfTurnOnOffAddonButton=f}function ServerStorage(){
```
### 37
```js
),Other.prototype.constructor=Other;function GroundItems(){var t=[],n=this,r=`/img/gui/item_frames/frames/item_frames.png`;let i=null,a=null;var s=0;this.init=function(){n.initFetch(),n.initDrop()};let c=t=>{let n=Engine.interface.getBottomPositioner().find(`.bottom-panel-of-bottom-positioner`),r={x:t.left,y:t.top},i=[[n.find(`.slots.right`),20],[n.find(`.slots.left`),20]];return checkPosIsCollisionWithLayers(r,i)};this.initDrop=function(){Engine.map.$worldPane.droppable({accept:`.item:not(.shop-item)`,drop:function(t,n){var r=n.draggable.data(`item`);if(Engine.trade||Engine.depo||Engine.shop||Engine.auctions||Engine.mails||
```
### 38
```js
n,r,i,a=null,s={},c={},l={},u=null,f=!1,p=null,m=null,h=null,_=null,v=null,y=null,b=null,x=null,C=!1;this.init=function(){n=Templates_default.get(`skills-window`),r=Templates_default.get(`additional-skill-panel`),i=Engine.interface.get$interfaceLayer().find(`.bottom-panel`),this.createWindow(),this.hideInterfaceItems(),this.initAdditionalHotKeys(),this.initBasicSkills(),this.initEqDragOpts(),this.initDroppable(),this.initMBattleWrapper(),Engine.interface.get$interfaceLayer().addClass(`show-skills-window`)},this.getOneStepSkillId=()=>`skill_`+SkillsData_default.specificSkills.ONE_STEP_ID,this.getNormalAttackSkillId=()=>`skill
```
### 39
```js
ttom-right`))},this.getSkills=function(){return s},this.getGroupedSkills=function(){return l},this.getBasicSkills=function(){return c},this.getActiveSkills=function(){return m},this.initAdditionalHotKeys=function(){Engine.interface.get$interfaceLayer().find(`.bottom-panel`).prepend(r)};let w=()=>Engine.interface.get$interfaceLayer().find(`.skill-usable-slots`);this.hideInterfaceItems=function(){let t=w();Engine.interface.get$interfaceLayer().find(`.bottom-panel>.slots`).css(`display`,`none`),t.css(`display`,`block`),getHeroLevel()>299&&$(`.end-game-overlay`).removeClass(`end-game-overlay`)},this.showInterfaceItems=function()
```
### 40
```js
nalHotKeys=function(){Engine.interface.get$interfaceLayer().find(`.bottom-panel`).prepend(r)};let w=()=>Engine.interface.get$interfaceLayer().find(`.skill-usable-slots`);this.hideInterfaceItems=function(){let t=w();Engine.interface.get$interfaceLayer().find(`.bottom-panel>.slots`).css(`display`,`none`),t.css(`display`,`block`),getHeroLevel()>299&&$(`.end-game-overlay`).removeClass(`end-game-overlay`)},this.showInterfaceItems=function(){let t=w();Engine.interface.get$interfaceLayer().find(`.bottom-panel>.slots`).css(`display`,`block`),t.css(`display`,`none`),Engine.interface.heroElements.checkAndSetEndGamePanel()},this.initDr
```
_Only first 40 of 67 matches shown._

## left-column
Matches: **45**

### 1
```js
"MAP_CANVAS"></canvas>-->         <canvas id="GAME_CANVAS" oncontextmenu="return false;"></canvas>         <div class="map-overlay filter-map-weather"></div>     </div>     <div class="pre-captcha"></div>     <div class="quick_messages"></div>     <div class="left-column main-column">         <div class="inner-wrapper"></div>         <div class="border">             <div class="wanted-mini"></div>         </div>     </div>     <div class="right-column main-column">         <div class="inner-wrapper">             <div class="right-main-column-wrapper">                 <div class="bottom-wrapper"></div>             </div>    
```
### 2
```js
t="100"></div>                     <div class="value"></div>                 </div>               </div>             </div>             <div class="gained-exp-indicator-light-mode"></div>                          <div data-trans="data-tip#iconchat" class="top-left-column-visibility-toggle column-visibility-toggle">                 <div class="icon"></div>                 <div class="amount interface-element-amount"></div>             </div>             <div data-trans="data-tip#eqcolumnshow" class="top-right-column-visibility-toggle column-visibility-toggle">                 <div class="icon"></div>                 <div cla
```
### 3
```js
ata-trans="data-tip#attach-battle-prediction-help-window"></div>         <div class="attach-battle-hot-skills-help-window  attach-icon" data-trans="data-tip#attach-battle-hot-skills-help-window"></div>         <div class="surrender"></div>         <div class="left-column">             <div class="scroll-wrapper">                 <div class="scroll-pane"></div>             </div>         </div>         <div class="stats-wrapper"></div>         <div class="buffs-wrapper"></div>         <div class="buttons-wrapper"></div>         <div class="right-column">             <div class="scroll-wrapper">                 <div class="sc
```
### 4
```js
      <div class="move-ways-wrapper">             <div class="move-ways-graphic ${getLang()}"></div>         </div>     </div>     <div class="content-header margin" data-trans="#fight-header#help"></div>     <div class="section-2 center">         <div class="left-column">             <div class="uppercase-header" data-trans="#start-fight-h#help"></div>             <div class="kind-fight margin"></div>             <div class="uppercase-header" data-trans="#move-in-fight-h#help"></div>             <div class="move-in-fight margin"></div>             <div class="uppercase-header" data-trans="#exp-h#help"></div>             <d
```
### 5
```js
div>         <div class="symbol ${getLang()}"></div>         <div class="text"></div>     </div> </div>`,TEMPLATES[`help-environment`]=`<div class="help-environment">     <div class="content-header margin" data-trans="#environment#help"></div>     <div class="left-column">         <div class="uppercase-header" data-trans="#dialog-h#help"></div>         <div class="margin" data-trans="#dialog-desc#help"></div>         <div class="uppercase-header" data-trans="#interface-customization-h#help"></div>         <div class="margin" data-trans="#interface-customization-desc#help"></div>         <div class="img-interface-customizati
```
### 6
```js
>     <div class="wrapper">         <div class="icon cl-icon"></div>     </div>     <div class="text"></div> </div>`,TEMPLATES[`help-premium`]=`<div class="help-premium">     <div class="content-header margin" data-trans="#premium#help"></div>     <div class="left-column">         <div class="uppercase-header margin" data-trans="#what-is-h#help"></div>         <div class="premium-offer margin" data-trans="#premium_offer#help"></div>         <div class="uppercase-header margin" data-trans="#boost-h#help"></div>         <div class="boost-account margin" data-trans="#boost-account#help"></div>         <div class="img-wrapper m
```
### 7
```js
 </div>     <div class="buttons action-buttons btns-spacing">     </div>     <div class="buttons sort-buttons btns-spacing">     </div>     <div class="line interface-element-line-1-background"></div> </div>`,TEMPLATES.clan=`<div class="clan">     <div class="left-column">         <div class="wood-background-1 interface-element-middle-1-background-stretch"></div>         <div class="clan-info interface-element-green-box-background">             <div class="clan-name">                 <span class="name"></span>             </div>             <div class="clan-level"></div>             <!--<div class="clan-emblem"></div>-->   
```
### 8
```js
ckground-stretch"></div>     </div> </div>`,TEMPLATES[`divide-panel`]=`<div class="divide-panel">     <!--<div class="header-wrapper">-->     <!--<div class="graphic"></div>-->     <!--<div class="green-panel-label"></div>-->     <!--</div>-->     <div class="left-column">     <div class="interface-element-middle-1-background-stretch"></div>         <!--<div class="top-left-column-graphics"></div>-->         <!--<div class="middle-left-column-graphics"></div>-->         <!--<div class="bottom-left-column-graphics"></div>-->         <div class="header-graphic interface-element-active-card-background-stretch"></div>         <
```
### 9
```js
lass="header-wrapper">-->     <!--<div class="graphic"></div>-->     <!--<div class="green-panel-label"></div>-->     <!--</div>-->     <div class="left-column">     <div class="interface-element-middle-1-background-stretch"></div>         <!--<div class="top-left-column-graphics"></div>-->         <!--<div class="middle-left-column-graphics"></div>-->         <!--<div class="bottom-left-column-graphics"></div>-->         <div class="header-graphic interface-element-active-card-background-stretch"></div>         <div class="left-column-header"></div>         <div class="search-wrapper search-item-wrapper">             <inpu
```
### 10
```js
>     <!--<div class="green-panel-label"></div>-->     <!--</div>-->     <div class="left-column">     <div class="interface-element-middle-1-background-stretch"></div>         <!--<div class="top-left-column-graphics"></div>-->         <!--<div class="middle-left-column-graphics"></div>-->         <!--<div class="bottom-left-column-graphics"></div>-->         <div class="header-graphic interface-element-active-card-background-stretch"></div>         <div class="left-column-header"></div>         <div class="search-wrapper search-item-wrapper">             <input class="search search-item"/>             <div class="search-x
```
### 11
```js
v>-->     <div class="left-column">     <div class="interface-element-middle-1-background-stretch"></div>         <!--<div class="top-left-column-graphics"></div>-->         <!--<div class="middle-left-column-graphics"></div>-->         <!--<div class="bottom-left-column-graphics"></div>-->         <div class="header-graphic interface-element-active-card-background-stretch"></div>         <div class="left-column-header"></div>         <div class="search-wrapper search-item-wrapper">             <input class="search search-item"/>             <div class="search-x" data-trans="data-tip#delete"></div>         </div>         <d
```
### 12
```js
n-graphics"></div>-->         <!--<div class="middle-left-column-graphics"></div>-->         <!--<div class="bottom-left-column-graphics"></div>-->         <div class="header-graphic interface-element-active-card-background-stretch"></div>         <div class="left-column-header"></div>         <div class="search-wrapper search-item-wrapper">             <input class="search search-item"/>             <div class="search-x" data-trans="data-tip#delete"></div>         </div>         <div class="left-scroll scroll-wrapper classic-bar">             <div class="scroll-pane"></div>         </div>     </div>     <div class="right-c
```
### 13
```js
e-graphic interface-element-middle-1-background"></div>         <div class="cards-header-wrapper"> <!--                <div class="header-background-graphic"></div>--> <!--                <div class="cards-header"></div>-->         </div>          <div class="left-column-auction-and-main-column-auction interface-element-vertical-wood">          </div>          <div class="left-column-auction"> <!--                <div class="scroll-wrapper left-column-scroll classic-bar">--> <!--                    <div class="scroll-pane">-->                     <div class="all-categories-auction"></div> <!--                    </div>--> <
```
### 14
```js
    <div class="header-background-graphic"></div>--> <!--                <div class="cards-header"></div>-->         </div>          <div class="left-column-auction-and-main-column-auction interface-element-vertical-wood">          </div>          <div class="left-column-auction"> <!--                <div class="scroll-wrapper left-column-scroll classic-bar">--> <!--                    <div class="scroll-pane">-->                     <div class="all-categories-auction"></div> <!--                    </div>--> <!--                </div>-->         </div>                    <div class="main-column-auction">             <div c
```
### 15
```js
    <div class="cards-header"></div>-->         </div>          <div class="left-column-auction-and-main-column-auction interface-element-vertical-wood">          </div>          <div class="left-column-auction"> <!--                <div class="scroll-wrapper left-column-scroll classic-bar">--> <!--                    <div class="scroll-pane">-->                     <div class="all-categories-auction"></div> <!--                    </div>--> <!--                </div>-->         </div>                    <div class="main-column-auction">             <div class="all-auction-info-wrapper">                 <div class="all-auct
```
### 16
```js
></span>     </div> </div>`,TEMPLATES[`draconite-shop`]=`<div class="draconite-shop">     <div class="draconite-shop-content">         <iframe class="sl-window"></iframe>     </div> </div>`,TEMPLATES[`addons-panel`]=`<div class="addons-panel">     <div class="left-column">         <div class="interface-element-middle-3-background-stretch"></div>         <div class="main-header">         <div class="interface-element-active-card-background-stretch"></div>             <div class="addon-list-label"></div>         </div>         <div class="left-scroll scroll-wrapper classic-bar">             <div class="scroll-pane">          
```
### 17
```js
></div> </div>`,TEMPLATES[`skills-window`]=`<div class="skills-window">     <!--<div class="header-wrapper">-->     <!--<div class="graphic"></div>-->     <!--<div class="edit-header-label" data-trans="#clickSkills"></div>-->     <!--</div>-->     <div class="left-column">         <div class="middle-graphic interface-element-middle-1-background"></div>         <div class="list-label-wrapper">             <div class="interface-element-active-card-background-stretch"></div>             <div class="list-border"></div>             <div class="list-label">                 <div class="label" data-trans="#skills_tip#buttons"></div
```
### 18
```js
d-list-and-right-description-window">     <!--<div class="main-header">-->          <!--<div class="card-background-wrapper">-->             <!--<div class="border-window-active-card-background-stretch"></div>-->          <!--</div>-->         <!--<div class="left-column-list-label"></div>-->     <!--</div>-->     <div class="right-column">         <!--<div class="middle-right-column-graphics"></div>-->         <div class="right-column-background interface-element-middle-2-background-stretch"></div>         <div class="right-header-graphic">             <div class="interface-element-active-card-background-stretch"></div>   
```
### 19
```js
reagents-label"></div>                 <div class="reagents-list">                     <div class="board"></div>                     <div class="all-items-wrapper"></div>                 </div>             </div>         </div>     </div>          <div class="left-column">         <!--<div class="middle-left-column-graphics"></div>-->         <div class="interface-element-middle-3-background-stretch"></div>         <div class="main-header">          <!--<div class="card-background-wrapper">-->         <div class="interface-element-active-card-background-stretch"></div>          <!--</div>-->         <div class="left-column-
```
### 20
```js
lass="reagents-list">                     <div class="board"></div>                     <div class="all-items-wrapper"></div>                 </div>             </div>         </div>     </div>          <div class="left-column">         <!--<div class="middle-left-column-graphics"></div>-->         <div class="interface-element-middle-3-background-stretch"></div>         <div class="main-header">          <!--<div class="card-background-wrapper">-->         <div class="interface-element-active-card-background-stretch"></div>          <!--</div>-->         <div class="left-column-list-label"></div>         </div>         <di
```
### 21
```js
terface-element-middle-3-background-stretch"></div>         <div class="main-header">          <!--<div class="card-background-wrapper">-->         <div class="interface-element-active-card-background-stretch"></div>          <!--</div>-->         <div class="left-column-list-label"></div>         </div>         <div class="search-wrapper search-in-left-column">             <input class="search" data-trans="placeholder#search"/>             <div class="search-x" data-trans="data-tip#delete"></div>         </div>         <!--<div class="bottom-left-column-graphics"></div>-->         <div class="left-scroll scroll-wrapper cla
```
### 22
```js
    <!--<div class="card-background-wrapper">-->         <div class="interface-element-active-card-background-stretch"></div>          <!--</div>-->         <div class="left-column-list-label"></div>         </div>         <div class="search-wrapper search-in-left-column">             <input class="search" data-trans="placeholder#search"/>             <div class="search-x" data-trans="data-tip#delete"></div>         </div>         <!--<div class="bottom-left-column-graphics"></div>-->         <div class="left-scroll scroll-wrapper classic-bar">             <div class="scroll-pane">                 <div class="items-list"></
```
### 23
```js
>         </div>         <div class="search-wrapper search-in-left-column">             <input class="search" data-trans="placeholder#search"/>             <div class="search-x" data-trans="data-tip#delete"></div>         </div>         <!--<div class="bottom-left-column-graphics"></div>-->         <div class="left-scroll scroll-wrapper classic-bar">             <div class="scroll-pane">                 <div class="items-list"></div>             </div>         </div>     </div>      <div class="bottom-row-panel">         <!--<div class="bottom-panel-graphics"></div>-->         <div class="interface-element-bottom-bar-backgr
```
### 24
```js
lass="start-lvl-wrapper-component"></div>             <div class="stop-lvl-wrapper-component"></div>         </div>`,TEMPLATES[`left-grouped-list-and-right-description-window2`]=`<div class="left-grouped-list-and-right-description-window">         <div class="left-column">             <div class="interface-element-middle-3-background-stretch"></div>             <div class="left-scroll scroll-wrapper classic-bar">                 <div class="scroll-pane">                     <div class="items-list"></div>                 </div>             </div>         </div>     </div>`,TEMPLATES[`left-grouped-list-right-column`]=`<div cl
```
### 25
```js
=`clan`&&!r&&a!=`clan_info`&&a!=`clan_list`||n.breakSwitch(l)||(n.setActiveTab(l,i),t==`clan`&&n.updateHeader(s),n.showChooseCard(t,a),$(`.scroll-wrapper`,`.clan-`+l+`-content`).trigger(`update`))})},this.setActiveTab=(t,n=null)=>{n=n===null?this.wnd.$.find(`.left-column .scroll-pane`):n,n.find(`.card[data-card="${t}"]`).addClass(`active`).siblings(`.card`).removeClass(`active`)},this.breakSwitch=function(t){var r=n[t+`Click`];if(!r)return!1;if(r())return!0},this.recruitClick=function(){return v.cardCallback(`recruit-main`),!1},this.listClick=function(){return _g(`clan&a=list&page=1`),y.hideFindPanel(),!1},this.membersClick
```
### 26
```js
a=!isset(s[r]),l=a?c[r]:s[r],f=a?this.createBasicSkill(r):this.createSkill(r,!0),p=Templates_default.get(`skill-description`),m=Templates_default.get(`button`).addClass(i?`black small`:`green small`),h=p.find(`.description`),_=p.find(`.skill-slider`);n.find(`.left-column #${r} .active`).hasClass(`quick-skill`)&&f.find(`.active`).addClass(`quick-skill`).tip(_t(`skill-icon-active`)),f.tip(``),t.createLearnButton(m),n.find(`.right-column`).find(`.description-wrapper`).html(p),t.createSkillSlider(_,l,i),t.createCost(+!i),h.html(l.desc),p.find(`.icon-wrapper`).html(f),p.find(`.name`).html(l.name),a||n.find(`.skill-learn-btn`).ht
```
### 27
```js
sList.add(`hide-right-header`),t.classList.add(`hide-left-header`)},x=()=>{h=$(t).find(`.left-scroll`),h.addScrollBar({track:!0})},C=t=>{u=t},w=()=>{a=new SearchComponent;let n={keyUpCallback:t=>{s&&s(t),O()},clearCallback:t=>{c&&c(t),O()},addClass:`search-in-left-column`};l&&(n.useDebounce=l),a.init(n),t.querySelector(`.left-column`).appendChild(a.getSearchWrapper()[0])},T=()=>t,D=r=>{n=Templates_default.get(`left-grouped-list-right-column`)[0];let i={track:!0};r.scrollBottomCallback&&(i.callback=r.scrollBottomCallback),$(n).find(`.right-scroll`).addScrollBar(i),t.appendChild(n)},O=()=>{h.trigger(`update`)},k=()=>{$(n).fin
```
### 28
```js
r`)},x=()=>{h=$(t).find(`.left-scroll`),h.addScrollBar({track:!0})},C=t=>{u=t},w=()=>{a=new SearchComponent;let n={keyUpCallback:t=>{s&&s(t),O()},clearCallback:t=>{c&&c(t),O()},addClass:`search-in-left-column`};l&&(n.useDebounce=l),a.init(n),t.querySelector(`.left-column`).appendChild(a.getSearchWrapper()[0])},T=()=>t,D=r=>{n=Templates_default.get(`left-grouped-list-right-column`)[0];let i={track:!0};r.scrollBottomCallback&&(i.callback=r.scrollBottomCallback),$(n).find(`.right-scroll`).addScrollBar(i),t.appendChild(n)},O=()=>{h.trigger(`update`)},k=()=>{$(n).find(`.right-scroll`).trigger(`update`)},A=()=>{$(n).find(`.right-
```
### 29
```js
init({minOptions:{keyUpClb:()=>this.startFilter(),clearClb:()=>this.startFilter()},maxOptions:{keyUpClb:()=>this.startFilter(),clearClb:()=>this.startFilter()}}),t.find(`.bottom-row-panel`).append($(a.getLevelFilter()))},this.initLabels=()=>{this.wnd.$.find(`.left-column-list-label`).html(_t(`exchange_list`,null,`item_changer`)),this.wnd.$.find(`.reagents-label`).html(_t(`reagents_label`))},this.updateScroll=function(){n.menuScrollUpdate(),n.rightScrollUpdate()},this.initNavigationMenu=function(){n=new NavigationMenu,n.init({createRightColumn:{attachMode:NavigationMenuData_default.ATTACH_MODE.SINGLE},createBottomPanel:{},se
```
### 30
```js
wOrHideBanners()},this.showConsoleNotif=function(){var n=`consoleNotif`;if(!$(`#`+n).length){var r=t.createNotif(n),i=_t(`warn_tip`,null,`static`);r.tip(i),r.click(function(){Engine.console.open()})}},this.isShowLeftColumn=()=>this.get$interfaceLayer().find(`.left-column.main-column`).css(`display`)!=`none`,this.createZoomOverlay=function(){var n=$(`.zoom-layer`);let r=getClickEventName();n.find(`.plus`).on(r,function(){t.clickIncreaseZoom()}),n.find(`.minus`).on(r,function(){t.clickDecreaseZoom()});var i=Templates_default.get(`button`).addClass(`green`);i.find(`.label`).html(_t(`out`,null,`logoff`));var a=Templates_default
```
### 31
```js
t t=null,n=!0,r=()=>{a(),i(),s()},i=()=>{getEngine().interface.get$gameWindowPositioner().find(`.chat-layer`).find(`.chat-overlay`).click(()=>{x(!1)})},a=()=>{t=Templates_default.get(`new-chat-window`)},s=()=>{getEngine().interface.get$interfaceLayer().find(`.left-column`).find(`.inner-wrapper`).append(t)},c=()=>t,l=(t,n,r)=>{let i=n||null,a=o$13.INPUT_CHANNEL_HEADER[t].inputWrapper,s=o$13.INPUT_CHANNEL_HEADER[a];getEngine().chatController.getChatChannelCardWrapper().setChannelCard(t),getEngine().chatController.getChatInputWrapper().setChannel(s,null,i,r),getEngine().chatController.getChatMessageWrapper().setChannelMessageW
```
### 32
```js
dateData=a,this.onClear=l}function HotKeys(){var t=this,n;this.hotKeys=null;let r=null;this.init=function(){this.initDefaultHotKeys(),this.hotKeys={},this.rebuildHotKeys()},this.initDefaultHotKeys=function(){let r=Engine.widgetsData.name,i=mobileCheck()?`.top-left-column-visibility-toggle.column-visibility-toggle`:`.widget-button:has(.icon.chat):not(.from-settings-panel)`,a=mobileCheck()?`.top-right-column-visibility-toggle.column-visibility-toggle`:`.widget-button:has(.icon.eq-show-icon):not(.from-settings-panel)`;n={},n[HotKeysData_default.name.move_up]=[`W`,!1,HotKeysData_default.type.LABEL,!1,HotKeysData_default.group.M
```
### 33
```js
L=t.name,n}createContent(){let t=Templates_default.get(`left-grouped-list-and-right-description-window`)[0];this.contentEl=this.wndEl.querySelector(`.item-craft-content`),this.contentEl.innerHTML=``,this.contentEl.appendChild(t),this.contentEl.querySelector(`.left-column .search-wrapper`)?.remove(),this.setBackground(),this.createTabContent()}setBackground(){let t=this.contentEl.querySelector(`.right-column .interface-element-middle-2-background-stretch`);t.classList.remove(`interface-element-middle-2-background-stretch`),t.classList.add(`interface-element-middle-1-background-stretch`)}createTabContent(){let t=document.crea
```
### 34
```js
ateElement(`div`);t.classList.add(`item-craft__tab-contents`);let n=this.contentEl.querySelector(`.right-column .scroll-pane`);n.innerHTML=``,n.appendChild(t)}initSearch(){this.searchComponent=new SearchComponent,this.searchComponent.init({addClass:`search-in-left-column`,keyUpCallback:()=>{this.startFilter()}}),this.contentEl.querySelector(`.left-column`).appendChild(this.searchComponent.getSearchWrapper()[0])}startFilter(){let t=(this.searchComponent.getSearchValue()||``).trim().toLowerCase();this.wndEl.querySelectorAll(`.one-item-on-divide-list`).forEach(n=>{let r=n.querySelector(`.name`)?.textContent?.toLowerCase()||``,
```
### 35
```js
erySelector(`.right-column .scroll-pane`);n.innerHTML=``,n.appendChild(t)}initSearch(){this.searchComponent=new SearchComponent,this.searchComponent.init({addClass:`search-in-left-column`,keyUpCallback:()=>{this.startFilter()}}),this.contentEl.querySelector(`.left-column`).appendChild(this.searchComponent.getSearchWrapper()[0])}startFilter(){let t=(this.searchComponent.getSearchValue()||``).trim().toLowerCase();this.wndEl.querySelectorAll(`.one-item-on-divide-list`).forEach(n=>{let r=n.querySelector(`.name`)?.textContent?.toLowerCase()||``,i=!t||r.includes(t);n.classList.toggle(`hide`,!i)})}closeAll(){this.engine.crafting[M
```
### 36
```js
-layer {                 //    overflow: visible;                 //}                  &.${i} {                     .new-chat-window {                         bottom:0px!important;                     }                     .chat-size-1 { 	                    .left-column.main-column {                             left: -261px;                         }  	                    .echh-layer, 	                    .game-layer, 	                    .layer.interface-layer .mini-map, 	                    .mAlert-layer .big-messages { 	                    	left: 0; 	                    } 	                    .layer.interface-layer .mai
```
### 37
```js
h-layer, 	                    .game-layer, 	                    .layer.interface-layer .mini-map, 	                    .mAlert-layer .big-messages { 	                    	left: 0; 	                    } 	                    .layer.interface-layer .main-column.left-column { 	                    	/*display: none;*/ 	                    	width: 0; 	                    	.border { 	                    	    display: none; 	                    	} 	                    } 	                    .left-column .inner-wrapper .chat-tpl .input-wrapper input { 	                    	width: 0; 	                    }                     }      
```
### 38
```js
r.interface-layer .main-column.left-column { 	                    	/*display: none;*/ 	                    	width: 0; 	                    	.border { 	                    	    display: none; 	                    	} 	                    } 	                    .left-column .inner-wrapper .chat-tpl .input-wrapper input { 	                    	width: 0; 	                    }                     }                 }  	        }              body[data-res="${n._920_X_555}"] { 			    .pre-captcha { 			        top:-22px; 			    } 			    .pre-captcha.show { 			        top:52px; 			    } 			    .interface-layer .battle-controller { 	
```
### 39
```js
         .interface-layer .top.positioner .bg,                 .interface-layer .bottom.positioner .bg {                     height: 50px;                 }                 .interface-layer {                     .right-column.main-column,                     .left-column.main-column,                     .game-layer {                         top: 50px;                         bottom : 50px;                     }                 }                 .b_wrapper {                     display: none;                 }                 .bottom.positioner .content .bottom-left-additional,                 .bottom.positioner .content .bo
```
### 40
```js
r=l,this.show=m,this.toggleAttach=_,this.hide=h,this.clear=f,this.appendMsg=u,this.addToLogLogContent=y,this.callProcedureOfAttach=v}function BattleMessages(){var t=this,n=null,r=null;this.forumLog=null;let i=!1,a;this.init=function(){r=$(`.battle-controller .left-column`),n=r.find(`.scroll-pane`),$(`.scroll-wrapper`,r).addScrollBar({track:!0}),a=new BattleLogHelpWindow,a.init()},this.addToLogLogContent=t=>{let r=t.clone();n[0].innerHTML+=t[0].innerHTML,a.addToLogLogContent(r)},this.open=function(){i=!0,this.forumLog=[],t.updateScroll(),t.showBattleLogHelpWindow()},this.updateScroll=function(){a.updateScrollbar(),$(`.scroll
```
_Only first 40 of 45 matches shown._

## right-column
Matches: **81**

### 1
```js
="pre-captcha"></div>     <div class="quick_messages"></div>     <div class="left-column main-column">         <div class="inner-wrapper"></div>         <div class="border">             <div class="wanted-mini"></div>         </div>     </div>     <div class="right-column main-column">         <div class="inner-wrapper">             <div class="right-main-column-wrapper">                 <div class="bottom-wrapper"></div>             </div>             <!--<div class="bottom-wrapper"></div>-->         </div>         <div class="border"></div>         <div class="extended-stats scroll-wrapper small-bar">             <div clas
```
### 2
```js
 class="top-left-column-visibility-toggle column-visibility-toggle">                 <div class="icon"></div>                 <div class="amount interface-element-amount"></div>             </div>             <div data-trans="data-tip#eqcolumnshow" class="top-right-column-visibility-toggle column-visibility-toggle">                 <div class="icon"></div>                 <div class="amount interface-element-amount"></div>             </div>                          <div class="top-left-widget-hamburger widget-hamburger">                 <div class="icon hamburger-icon"></div>                 <div class="amount interface-ele
```
### 3
```js
lert-item`]=`<div class="alert-item">     <div class="alert-item-name"></div>     <div class="alert-item-icon"></div> </div>`,TEMPLATES[`new-item`]=`<div class="new-item"></div>`,TEMPLATES.afterUseBottonItem=`<div class="afterUseBottonItem"></div>`,TEMPLATES[`right-column-notif`]=`<div class="right-column-notif">     <span class="notif-value c-amount"></span> </div>`,TEMPLATES[`popup-menu`]=`<div class="popup-menu">   <div class="scroll-wrapper small-bar">       <div class="scroll-pane popup-menu__list"></div>   </div> </div>`,TEMPLATES[`popup-menu-header`]=`<div class="popup-menu__header"></div>`,TEMPLATES[`menu-item`]=`<di
```
### 4
```js
m">     <div class="alert-item-name"></div>     <div class="alert-item-icon"></div> </div>`,TEMPLATES[`new-item`]=`<div class="new-item"></div>`,TEMPLATES.afterUseBottonItem=`<div class="afterUseBottonItem"></div>`,TEMPLATES[`right-column-notif`]=`<div class="right-column-notif">     <span class="notif-value c-amount"></span> </div>`,TEMPLATES[`popup-menu`]=`<div class="popup-menu">   <div class="scroll-wrapper small-bar">       <div class="scroll-pane popup-menu__list"></div>   </div> </div>`,TEMPLATES[`popup-menu-header`]=`<div class="popup-menu__header"></div>`,TEMPLATES[`menu-item`]=`<div class="menu-item"></div>`,TEMPLA
```
### 5
```js
nt-grid-border items-grid scroll-wrapper small-bar">             <div class="interface-element-item-slot-grid-stretch"></div>             <div class="scroll-pane"></div>             <div class="shop-info-wrapper"></div>         </div>         <div class="shop-right-column">             <div class="buy-items interface-element-grid-border items-grid ">                 <div class="interface-element-item-slot-grid-stretch"></div>                 <span class="label interface-element-grid-border" data-trans="#buying_items#shop"></span>             </div>             <div class="sell-items interface-element-grid-border items-grid">
```
### 6
```js
 <div class="scroll-wrapper">                 <div class="scroll-pane"></div>             </div>         </div>         <div class="stats-wrapper"></div>         <div class="buffs-wrapper"></div>         <div class="buttons-wrapper"></div>         <div class="right-column">             <div class="scroll-wrapper">                 <div class="scroll-pane">                     <div class="turn-prediction"></div>                 </div>             </div>             <div class="battle-end-layer" data-trans="#battle_ended#battle"></div>         </div>          <div class="battle-bar-light-mode interface-element-progress-bar-2 en
```
### 7
```js
div>             <div class="img-wrapper margin">                 <div class="level-img ${getLang()}"></div>             </div>             <div class="exp-level-info margin  justify" data-trans="#exp-level-info#help"></div>         </div>         <div class="right-column">             <div class="uppercase-header" data-trans="#skills-h#help"></div>             <div class="skill-desc margin justify" data-trans="#skills-desc#help"></div>             <div class="img-wrapper margin">                 <div class="skill-passive-active-img ${getLang()}"></div>             </div>             <div class="skill-passive-active-desc mar
```
### 8
```js
ass="uppercase-header" data-trans="#quests-h#help"></div>         <div class="margin" data-trans="#quests-desc#help"></div>         <div class="img-wrapper margin">             <div class="npc-img ${getLang()}"></div>         </div>     </div>     <div class="right-column">         <div class="uppercase-header" data-trans="#quests-window-h#help"></div>         <div class="margin" data-trans="#quests-window-desc#help"></div>         <div class="img-wrapper margin">             <div class="quest-img ${getLang()}"></div>         </div>         <div class="uppercase-header" data-trans="#shop-h#help"></div>         <div data-tran
```
### 9
```js
rgin" data-trans="#boost-h#help"></div>         <div class="boost-account margin" data-trans="#boost-account#help"></div>         <div class="img-wrapper margin">             <div class="boost-img ${getLang()}"></div>         </div>     </div>     <div class="right-column">         <div class="uppercase-header margin" data-trans="#where-is-shop-h#help"></div>         <div class="margin" data-trans="#where-is-shop-desc#help"></div>         <div class="img-wrapper margin">             <div class="premium-img ${getLang()}"></div>         </div>         <div class="uppercase-header margin" data-trans="#sl-investment-h#help"></di
```
### 10
```js
     </div>         <!--<div class="clan-list-repeat"></div>-->         <!--<div class="clan-list-bottom"></div>-->         <div class="scroll-wrapper classic-bar">             <div class="scroll-pane tabs-nav"></div>         </div>     </div>     <div class="right-column">         <div class="interface-element-middle-2-background-stretch"></div>         <div class="card-content"></div>     </div> </div>`,TEMPLATES[`clan-list-content`]=`<div class="clan-list-content">     <div class="clan-list-show-btn"></div>     <div class="table-header-wrapper">         <table class="table-header clan-list-table-header interface-element-t
```
### 11
```js
lass="search search-item"/>             <div class="search-x" data-trans="data-tip#delete"></div>         </div>         <div class="left-scroll scroll-wrapper classic-bar">             <div class="scroll-pane"></div>         </div>     </div>     <div class="right-column">     <div class="interface-element-middle-1-background-stretch"></div>         <!--<div class="location-graphics"></div>-->         <!--<div class="middle-graphics"></div>-->         <div class="header-graphic interface-element-active-card-background-stretch"></div>         <div class="right-column-header"></div>         <div class="right-scroll scroll-wra
```
### 12
```js
element-middle-1-background-stretch"></div>         <!--<div class="location-graphics"></div>-->         <!--<div class="middle-graphics"></div>-->         <div class="header-graphic interface-element-active-card-background-stretch"></div>         <div class="right-column-header"></div>         <div class="right-scroll scroll-wrapper classic-bar">             <div class="scroll-pane"></div>         </div>     </div>     <div class="bottom-part">         <div class="interface-element-bottom-bar-background-stretch"></div>         <!--<div class="bottom-panel-graphics"></div>-->     </div> </div>`,TEMPLATES.table=`     <table c
```
### 13
```js
 <div class="addon-list-label"></div>         </div>         <div class="left-scroll scroll-wrapper classic-bar">             <div class="scroll-pane">                 <div class="addon-list"></div>             </div>         </div>     </div>     <div class="right-column">         <div class="interface-element-middle-2-background-stretch"></div>         <div class="right-header-graphic">             <div class="interface-element-active-card-background-stretch"></div>         </div>         <div class="addon-header">             <div class="img-wrapper">                 <div class="widget-button red no-hover">               
```
### 14
```js
</div>             </div>         </div>         <div class="scroll-wrapper classic-bar skills-wrapper">             <div class="scroll-pane">                 <div class="description-wrapper"></div>             </div>         </div>     </div>     <div class="right-column">         <div class="middle-graphic interface-element-middle-2-background"></div>         <!--<div class="maku-wood"></div>-->         <div class="points-header-wrapper">             <div class="interface-element-active-card-background-stretch"></div>             <div class="skills-points-wrapper">                 <div class="skills-points-description" dat
```
### 15
```js
r">-->          <!--<div class="card-background-wrapper">-->             <!--<div class="border-window-active-card-background-stretch"></div>-->          <!--</div>-->         <!--<div class="left-column-list-label"></div>-->     <!--</div>-->     <div class="right-column">         <!--<div class="middle-right-column-graphics"></div>-->         <div class="right-column-background interface-element-middle-2-background-stretch"></div>         <div class="right-header-graphic">             <div class="interface-element-active-card-background-stretch"></div>         </div>         <div class="right-column-header"></div>         
```
### 16
```js
d-wrapper">-->             <!--<div class="border-window-active-card-background-stretch"></div>-->          <!--</div>-->         <!--<div class="left-column-list-label"></div>-->     <!--</div>-->     <div class="right-column">         <!--<div class="middle-right-column-graphics"></div>-->         <div class="right-column-background interface-element-middle-2-background-stretch"></div>         <div class="right-header-graphic">             <div class="interface-element-active-card-background-stretch"></div>         </div>         <div class="right-column-header"></div>         <!--<div class="paper-graphics"></div>-->     
```
### 17
```js
dow-active-card-background-stretch"></div>-->          <!--</div>-->         <!--<div class="left-column-list-label"></div>-->     <!--</div>-->     <div class="right-column">         <!--<div class="middle-right-column-graphics"></div>-->         <div class="right-column-background interface-element-middle-2-background-stretch"></div>         <div class="right-header-graphic">             <div class="interface-element-active-card-background-stretch"></div>         </div>         <div class="right-column-header"></div>         <!--<div class="paper-graphics"></div>-->         <div class="right-scroll scroll-wrapper classic-b
```
### 18
```js
->         <div class="right-column-background interface-element-middle-2-background-stretch"></div>         <div class="right-header-graphic">             <div class="interface-element-active-card-background-stretch"></div>         </div>         <div class="right-column-header"></div>         <!--<div class="paper-graphics"></div>-->         <div class="right-scroll scroll-wrapper classic-bar">             <div class="scroll-pane">                 <div class="additional-container"></div>                 <div class="reagents-label"></div>                 <div class="reagents-list">                     <div class="board"></d
```
### 19
```js
iv>             <div class="left-scroll scroll-wrapper classic-bar">                 <div class="scroll-pane">                     <div class="items-list"></div>                 </div>             </div>         </div>     </div>`,TEMPLATES[`left-grouped-list-right-column`]=`<div class="left-grouped-list-right-column right-column">           <div class="right-column-background interface-element-middle-1-background-stretch"></div>           <div class="right-scroll scroll-wrapper classic-bar">               <div class="scroll-pane">               </div>           </div>       </div>`,TEMPLATES[`left-grouped-list-right-column-
```
### 20
```js
-wrapper classic-bar">                 <div class="scroll-pane">                     <div class="items-list"></div>                 </div>             </div>         </div>     </div>`,TEMPLATES[`left-grouped-list-right-column`]=`<div class="left-grouped-list-right-column right-column">           <div class="right-column-background interface-element-middle-1-background-stretch"></div>           <div class="right-scroll scroll-wrapper classic-bar">               <div class="scroll-pane">               </div>           </div>       </div>`,TEMPLATES[`left-grouped-list-right-column-bottom-row-panel`]=`   <div class="left-groupe
```
### 21
```js
sic-bar">                 <div class="scroll-pane">                     <div class="items-list"></div>                 </div>             </div>         </div>     </div>`,TEMPLATES[`left-grouped-list-right-column`]=`<div class="left-grouped-list-right-column right-column">           <div class="right-column-background interface-element-middle-1-background-stretch"></div>           <div class="right-scroll scroll-wrapper classic-bar">               <div class="scroll-pane">               </div>           </div>       </div>`,TEMPLATES[`left-grouped-list-right-column-bottom-row-panel`]=`   <div class="left-grouped-list-right-
```
### 22
```js
"scroll-pane">                     <div class="items-list"></div>                 </div>             </div>         </div>     </div>`,TEMPLATES[`left-grouped-list-right-column`]=`<div class="left-grouped-list-right-column right-column">           <div class="right-column-background interface-element-middle-1-background-stretch"></div>           <div class="right-scroll scroll-wrapper classic-bar">               <div class="scroll-pane">               </div>           </div>       </div>`,TEMPLATES[`left-grouped-list-right-column-bottom-row-panel`]=`   <div class="left-grouped-list-right-column-bottom-row-panel bottom-row-pa
```
### 23
```js
ht-column-background interface-element-middle-1-background-stretch"></div>           <div class="right-scroll scroll-wrapper classic-bar">               <div class="scroll-pane">               </div>           </div>       </div>`,TEMPLATES[`left-grouped-list-right-column-bottom-row-panel`]=`   <div class="left-grouped-list-right-column-bottom-row-panel bottom-row-panel">       <div class="interface-element-bottom-bar-background-stretch"></div>   </div>`,TEMPLATES[`divide-list-group`]=`<div class="divide-list-group">     <div class="group-header">         <div class="card-graphic interface-element-active-card-border-image"><
```
### 24
```js
"></div>           <div class="right-scroll scroll-wrapper classic-bar">               <div class="scroll-pane">               </div>           </div>       </div>`,TEMPLATES[`left-grouped-list-right-column-bottom-row-panel`]=`   <div class="left-grouped-list-right-column-bottom-row-panel bottom-row-panel">       <div class="interface-element-bottom-bar-background-stretch"></div>   </div>`,TEMPLATES[`divide-list-group`]=`<div class="divide-list-group">     <div class="group-header">         <div class="card-graphic interface-element-active-card-border-image"></div>         <div class="label"></div>         <div class="direct
```
### 25
```js
t(`no`),callback:function(){return!0}}])},window.goToMainPage=()=>{let t=getMainDomain();window.location.href=`https://margonem.${t}`},window.hideInterface=function(){$(`.top.positioner`).css(`display`,`none`),$(`.bottom.positioner`).css(`display`,`none`),$(`.right-column.main-column`).css(`display`,`none`),Engine.interface.get$gameLayer().css({top:`0px`,right:`0px`,bottom:`0px`})},window.getFreeIdOfObject=(t,n)=>{let r=isset$4(n)?n:0;for(;isset$4(t[r]);)r++;return r},window.getFreeIdOfArray=(t,n)=>{let r={};for(let n in t){let i=t[n].id;r[i]=!0}return getFreeIdOfObject(r,n)},window.getCookie=getCookie$1,window.toggleFullScr
```
### 26
```js
wPreviewItemInShop(u.cl)&&!l){t.setShopType();let n=$(`<div>`).addClass(`info-icon shop-info-icon`);l=!0,ItemClass.isOutfitCl(u.cl)&&n.tip(_t(`action_info_outfit`)),ItemClass.isPetCl(u.cl)&&n.tip(_t(`action_info`,null,`pet`)),t.wnd.$.find(`.shop-content .shop-right-column`).append(n)}t.setLabel()},this.buySeriallyItem=function(n,r){for(var i=0;i<n;i++)t.basket.buyItem(r)},this.unBuySeriallyItem=function(n,r,i,a){for(var s=0;s<n;s++)if(t.basket.unbuyItem(r,i,a),i.parent().length<1){getEngine().interface.removePopupMenu();return}},this.alertWindow=function(n){var r=[_t(`how_want_to_buy`,null,`item`),_t(`cancel`,null,`buttons`)
```
### 27
```js
ion(){r.changeScrollWrapperPos(76),r.fillLeftColumn(),n.wnd.$.find(`.MB-wrapper`).css(`display`,`none`),n.wnd.$.find(`.empty`).css(`display`,`none`),n.wnd.$.find(`.edit-header-label`).text(_t(`mbattle`))},this.changeScrollWrapperPos=function(t){n.wnd.$.find(`.right-column`).find(`.scroll-wrapper`).css(`top`,t+`px`)},this.getButton=function(t,r){var i=Templates_default.get(`button`).addClass(t);return i.find(`.label`).html(n.tLang(r)),i},this.fillLeftColumn=function(){var s=t.find(`.skills-wrapper > .scroll-pane`),l=[],u=null;l.push($(`<div/>`,{class:`description-wrapper`,html:n.tLang(`mb_add_to_list_desc`)})),l.push(n.create
```
### 28
```js
reached`,null,`skills`));var t=$(this).attr(`id`).split(`_`).pop();a.push(t),r.save()})},this.fillRightColumn=function(){var i=Templates_default.get(`MBEditor`),a=this.getButton(`small green`,`clear-list`),l=this.getButton(`small green`,`save-btn`),u=t.find(`.right-column`);$(`.description-wrapper`,u).html(i);let f=!0;for(var p=[],m=null,h=0;h<20;h++)m=Templates_default.get(`single-skill-row`).attr(`id`,`mb_list_`+h),m.find(`.number`).html(h+1+`.`),h<c?m.addClass(`usable`):(r.addBuyButtons(m,h),f?f=!1:m.addClass(`disable`)),p.push(m),r.fillButtonsCallbacks(m);n.wnd.$.find(`.skills-points-description`).html(_t(`mbattle`)),n.w
```
### 29
```js
ditor(()=>{r.changeScrollWrapperPos(42),n.wnd.$.find(`.MB-wrapper`).css(`display`,`block`),n.wnd.$.find(`.skills-points-description`).html(_t(`skills_points_description`,null,`skills`)),n.wnd.$.find(`.edit-header-label`).text(_t(`clickSkills`)),n.wnd.$.find(`.right-column`).find(`.skills-points`).removeClass(`d-none`)})},this.clearList=function(){a=[],r.save()},this.fillButtonCallbacks=function(n){n.find(`.up-arrow`).click(function(){r.arrowManager(`up`,$(this).parent())}),n.find(`.down-arrow`).click(function(){r.arrowManager(`down`,$(this).parent())}),n.find(`.remove-cross`).click(function(){r.arrowManager(`cross`,$(this).p
```
### 30
```js
ction(t){return s[t].kind===`unav`},this.getDescription=function(n){var r=t.tLang(`skill_req_desc_new %lvl% %points%`,{"%lvl%":n,"%points%":n-25});return Templates_default.get(`skills-description-wrapper`).html(r)},this.updateSkillsLearnt=function(t){n.find(`.right-column`).find(`.skills-points .skills_learnt`).text(t)},this.updateSkillsTotal=function(t){n.find(`.right-column`).find(`.skills-points .skills_total`).text(t)},this.fillRightColumn=function(){n.find(`.right-column`).find(`.description-wrapper`).html(``)},this.createResetButton=function(n){var r=50,i=Templates_default.get(`button`).addClass(`purple small`),a=round
```
### 31
```js
% %points%`,{"%lvl%":n,"%points%":n-25});return Templates_default.get(`skills-description-wrapper`).html(r)},this.updateSkillsLearnt=function(t){n.find(`.right-column`).find(`.skills-points .skills_learnt`).text(t)},this.updateSkillsTotal=function(t){n.find(`.right-column`).find(`.skills-points .skills_total`).text(t)},this.fillRightColumn=function(){n.find(`.right-column`).find(`.description-wrapper`).html(``)},this.createResetButton=function(n){var r=50,i=Templates_default.get(`button`).addClass(`purple small`),a=round(r,10),s=$(`<span/>`,{class:`reset`,html:t.tLang(`reset_btn`)+`: `+a}),c=$(`<span/>`).addClass(`small-drac
```
### 32
```js
ml(r)},this.updateSkillsLearnt=function(t){n.find(`.right-column`).find(`.skills-points .skills_learnt`).text(t)},this.updateSkillsTotal=function(t){n.find(`.right-column`).find(`.skills-points .skills_total`).text(t)},this.fillRightColumn=function(){n.find(`.right-column`).find(`.description-wrapper`).html(``)},this.createResetButton=function(n){var r=50,i=Templates_default.get(`button`).addClass(`purple small`),a=round(r,10),s=$(`<span/>`,{class:`reset`,html:t.tLang(`reset_btn`)+`: `+a}),c=$(`<span/>`).addClass(`small-draconite`);i.find(`.label`).html([s,c]),i.click(function(){_g(`skills&reset=1`)}),n.html(i)},this.initBat
```
### 33
```js
ss(i?`black small`:`green small`),h=p.find(`.description`),_=p.find(`.skill-slider`);n.find(`.left-column #${r} .active`).hasClass(`quick-skill`)&&f.find(`.active`).addClass(`quick-skill`).tip(_t(`skill-icon-active`)),f.tip(``),t.createLearnButton(m),n.find(`.right-column`).find(`.description-wrapper`).html(p),t.createSkillSlider(_,l,i),t.createCost(+!i),h.html(l.desc),p.find(`.icon-wrapper`).html(f),p.find(`.name`).html(l.name),a||n.find(`.skill-learn-btn`).html(m),s[r],this.showStats(SkillTip_default.getStats(l),l.cLvl,l.mLvl),i&&!a?a||n.find(`.skill-learn-btn > .button`).removeClass(`green`).addClass(`black`):l.cLvl==l.mL
```
### 34
```js
et n={keyUpCallback:t=>{s&&s(t),O()},clearCallback:t=>{c&&c(t),O()},addClass:`search-in-left-column`};l&&(n.useDebounce=l),a.init(n),t.querySelector(`.left-column`).appendChild(a.getSearchWrapper()[0])},T=()=>t,D=r=>{n=Templates_default.get(`left-grouped-list-right-column`)[0];let i={track:!0};r.scrollBottomCallback&&(i.callback=r.scrollBottomCallback),$(n).find(`.right-scroll`).addScrollBar(i),t.appendChild(n)},O=()=>{h.trigger(`update`)},k=()=>{$(n).find(`.right-scroll`).trigger(`update`)},A=()=>{$(n).find(`.right-scroll`).trigger(`scrollTop`)},j=()=>{$(n).find(`.right-scroll`).trigger(`updateBarPos`)},M=()=>{r=Templates_d
```
### 35
```js
pendChild(n)},O=()=>{h.trigger(`update`)},k=()=>{$(n).find(`.right-scroll`).trigger(`update`)},A=()=>{$(n).find(`.right-scroll`).trigger(`scrollTop`)},j=()=>{$(n).find(`.right-scroll`).trigger(`updateBarPos`)},M=()=>{r=Templates_default.get(`left-grouped-list-right-column-bottom-row-panel`)[0],t.appendChild(r)},P=()=>{for(let t in f)I(t)?f[t].classList.add(`hide`):f[t].classList.remove(`hide`);F()},F=()=>{for(let t in f){let n=f[t].querySelectorAll(`.group-list .one-item-on-divide-list:not(.hide)`).length;f[t].querySelector(`.amount`).innerHTML=n}},I=t=>{if(!B(t))return!1;let n=f[t].querySelectorAll(`.one-item-on-divide-list
```
### 36
```js
()),i.addEventListener(getClickEventName(),()=>{i.classList.contains(`active`)&&(r.getNavigationMenu().querySelectorAll(`.divide-list-group`).forEach(t=>{t!==i&&t.classList.remove(`active`)}),t.onClickEvent(n))})}},this.modifyContent=function(){var r=n.find(`.right-column`),i=$(`<div>`).addClass(`right-header-graphic`).append($(`<div>`).addClass(`interface-element-active-card-background-stretch`)),c=$(`<div>`).addClass(`city-name`),l=$(`<div>`).addClass(`right-column-header`).append(c);r.find(`.right-scroll`).before(i,l);var u=$(`<div>`).addClass(`mini-map-wrapper`),f=$(`<div>`).addClass(`mini-map-positioner`);u.append(f),n.
```
### 37
```js
ckEvent(n))})}},this.modifyContent=function(){var r=n.find(`.right-column`),i=$(`<div>`).addClass(`right-header-graphic`).append($(`<div>`).addClass(`interface-element-active-card-background-stretch`)),c=$(`<div>`).addClass(`city-name`),l=$(`<div>`).addClass(`right-column-header`).append(c);r.find(`.right-scroll`).before(i,l);var u=$(`<div>`).addClass(`mini-map-wrapper`),f=$(`<div>`).addClass(`mini-map-positioner`);u.append(f),n.find(`.right-scroll .scroll-pane`).append(u);var p=$(`<div>`).addClass(`city-buffer-wrapper`),m=$(`<div>`).html(_t(`city_loading`)).addClass(`city-buffer`);p.append(m),r.append(p);var h=Templates_def
```
### 38
```js
terfaceLayerHeight=()=>this.get$interfaceLayer().height(),this.initPositioners=()=>{_=this.get$interfaceLayer().find(`.bottom.positioner`),v=this.get$interfaceLayer().find(`.top.positioner`),y=this.get$interfaceLayer().find(`.under-top.positioner`),b=f.find(`.right-column.main-column`)},this.get$rightColumn=()=>b,this.getBottomPositioner=()=>_,this.getTopPositioner=()=>v,this.getUnderTopPositioner=()=>y,this.init$MAP_CANVAS=()=>{m=$(`#MAP_CANVAS`)},this.init$GAME_CANVAS=()=>{h=$(`#GAME_CANVAS`)},this.init$gameWindowPositioner=()=>{f=$(`.game-window-positioner`)};let X=()=>{let t=t=>{let n=[[_t(`copy-location-cords`),function
```
### 39
```js
th-additional-bag`).addClass(`equipment-wrapper`);F.find(`.equipment-wrapper`).replaceWith(l);let u=Ie();u.append(F),u.append(Templates_default.get(`battle-set-wrapper`)),u.append(P),u.append($(`<div>`).addClass(`tutorial-banner-anchor`))};let Ie=()=>f.find(`.right-column`).find(`.inner-wrapper`).find(`.right-main-column-wrapper`);this.clearCanvasCursor=()=>{let t=ColliderData_default.CURSOR;h.removeClass(`${t.DO_ACTION} ${t.PICK_UP} ${t.DIALOGUE} ${t.ATTACK}`)},this.addToGameWindowPositioner=t=>{f.append(t)},this.tooMoreZoomOut=function(){return $(`body`).width()>$(window).width()*2},this.initChangePlayer=()=>{Engine.change
```
### 40
```js
howItemDetails=function(){isSettingsOptionsShowItemDetailsOn()?$(`body`).removeClass(`item-details-off`):$(`body`).addClass(`item-details-off`)},this.setLangClass=function(){$(`body`).addClass(`lang-${_l()}`)},this.createNotif=t=>{let n=Templates_default.get(`right-column-notif`);return this.addToQueue(t),n.attr(`id`,t),this.get$interfaceLayer().find(`.bottom-right`).find(`.game-notifications`).append(n),this.setPositionNotif(t),n},this.deleteNotif=function(n){var i=this.getNotifIndex(n);i!==null&&($(`#`+n).remove(),r.splice(i,1),t.rebuildPosAllNotif())},this.setPositionNotif=function(t){var n=this.getNotifIndex(t);if(n!==nu
```
_Only first 40 of 81 matches shown._

## mini-map
Matches: **70**

### 1
```js
 interface-element-one-item-slot-2" slot="6"></div>         <div class="skill-usable-slot interface-element-one-item-slot-2" slot="5"></div>         <div class="skill-usable-slot interface-element-one-item-slot-2" slot="4"></div>     </div> </div>`,TEMPLATES[`mini-map-controller`]=`<div class="mini-map-controller mini-map">     <!--<div class="mini-map-header">-->     <!--<div class="graphic"></div>-->     <!--<div class="mini-map-label"></div>-->     <!--</div>-->     <div class="mini-map-map">         <div class="graphic interface-element-middle-1-background"></div>         <div class="mini-local-map"></div>         <d
```
### 2
```js
 slot="6"></div>         <div class="skill-usable-slot interface-element-one-item-slot-2" slot="5"></div>         <div class="skill-usable-slot interface-element-one-item-slot-2" slot="4"></div>     </div> </div>`,TEMPLATES[`mini-map-controller`]=`<div class="mini-map-controller mini-map">     <!--<div class="mini-map-header">-->     <!--<div class="graphic"></div>-->     <!--<div class="mini-map-label"></div>-->     <!--</div>-->     <div class="mini-map-map">         <div class="graphic interface-element-middle-1-background"></div>         <div class="mini-local-map"></div>         <div class="mini-global-map-overflow"
```
### 3
```js
     <div class="skill-usable-slot interface-element-one-item-slot-2" slot="5"></div>         <div class="skill-usable-slot interface-element-one-item-slot-2" slot="4"></div>     </div> </div>`,TEMPLATES[`mini-map-controller`]=`<div class="mini-map-controller mini-map">     <!--<div class="mini-map-header">-->     <!--<div class="graphic"></div>-->     <!--<div class="mini-map-label"></div>-->     <!--</div>-->     <div class="mini-map-map">         <div class="graphic interface-element-middle-1-background"></div>         <div class="mini-local-map"></div>         <div class="mini-global-map-overflow">             <div c
```
### 4
```js
lot interface-element-one-item-slot-2" slot="5"></div>         <div class="skill-usable-slot interface-element-one-item-slot-2" slot="4"></div>     </div> </div>`,TEMPLATES[`mini-map-controller`]=`<div class="mini-map-controller mini-map">     <!--<div class="mini-map-header">-->     <!--<div class="graphic"></div>-->     <!--<div class="mini-map-label"></div>-->     <!--</div>-->     <div class="mini-map-map">         <div class="graphic interface-element-middle-1-background"></div>         <div class="mini-local-map"></div>         <div class="mini-global-map-overflow">             <div class="mini-global-map"></div>  
```
### 5
```js
-usable-slot interface-element-one-item-slot-2" slot="4"></div>     </div> </div>`,TEMPLATES[`mini-map-controller`]=`<div class="mini-map-controller mini-map">     <!--<div class="mini-map-header">-->     <!--<div class="graphic"></div>-->     <!--<div class="mini-map-label"></div>-->     <!--</div>-->     <div class="mini-map-map">         <div class="graphic interface-element-middle-1-background"></div>         <div class="mini-local-map"></div>         <div class="mini-global-map-overflow">             <div class="mini-global-map"></div>         </div>         <div class="mini-map-mouse-move"></div>     </div>     <di
```
### 6
```js
iv>     </div> </div>`,TEMPLATES[`mini-map-controller`]=`<div class="mini-map-controller mini-map">     <!--<div class="mini-map-header">-->     <!--<div class="graphic"></div>-->     <!--<div class="mini-map-label"></div>-->     <!--</div>-->     <div class="mini-map-map">         <div class="graphic interface-element-middle-1-background"></div>         <div class="mini-local-map"></div>         <div class="mini-global-map-overflow">             <div class="mini-global-map"></div>         </div>         <div class="mini-map-mouse-move"></div>     </div>     <div class="mini-map-panel">         <div class="interface-elem
```
### 7
```js
ni-map-map">         <div class="graphic interface-element-middle-1-background"></div>         <div class="mini-local-map"></div>         <div class="mini-global-map-overflow">             <div class="mini-global-map"></div>         </div>         <div class="mini-map-mouse-move"></div>     </div>     <div class="mini-map-panel">         <div class="interface-element-active-card-background-stretch"></div>         <div class="mini-map-buttons"></div>     </div>     <div class="mini-map-content"></div> </div>`,TEMPLATES[`extended-stats-tpl`]=`<div class="extended-stats-tpl scroll-pane">      <div class="stats-section">    
```
### 8
```js
ent-middle-1-background"></div>         <div class="mini-local-map"></div>         <div class="mini-global-map-overflow">             <div class="mini-global-map"></div>         </div>         <div class="mini-map-mouse-move"></div>     </div>     <div class="mini-map-panel">         <div class="interface-element-active-card-background-stretch"></div>         <div class="mini-map-buttons"></div>     </div>     <div class="mini-map-content"></div> </div>`,TEMPLATES[`extended-stats-tpl`]=`<div class="extended-stats-tpl scroll-pane">      <div class="stats-section">         <h3 data-trans="stats_attack"></h3>          <div 
```
### 9
```js
rflow">             <div class="mini-global-map"></div>         </div>         <div class="mini-map-mouse-move"></div>     </div>     <div class="mini-map-panel">         <div class="interface-element-active-card-background-stretch"></div>         <div class="mini-map-buttons"></div>     </div>     <div class="mini-map-content"></div> </div>`,TEMPLATES[`extended-stats-tpl`]=`<div class="extended-stats-tpl scroll-pane">      <div class="stats-section">         <h3 data-trans="stats_attack"></h3>          <div class="damage-section">             <!-- filled in runime from few values !-->             <div class="stat-row da
```
### 10
```js
iv>         </div>         <div class="mini-map-mouse-move"></div>     </div>     <div class="mini-map-panel">         <div class="interface-element-active-card-background-stretch"></div>         <div class="mini-map-buttons"></div>     </div>     <div class="mini-map-content"></div> </div>`,TEMPLATES[`extended-stats-tpl`]=`<div class="extended-stats-tpl scroll-pane">      <div class="stats-section">         <h3 data-trans="stats_attack"></h3>          <div class="damage-section">             <!-- filled in runime from few values !-->             <div class="stat-row damage-normal warrior-stats" data-herostat="damage-nor
```
### 11
```js
 class="grid"></div> `,TEMPLATES.depo_backlight=`<div class="depo_backlight"></div>`,TEMPLATES[`depo-filter`]=`<div class="depo-filter">     <div class="menu-wrapper">         <div class="menu"></div>     </div>     <div class="back"></div> </div>`,TEMPLATES[`mini-map-local-content`]=`<div class="mini-map-local-content">     <div class="graphic interface-element-middle-1-background-stretch"></div>     <div class="scroll-wrapper">         <div class="scroll-pane"></div>     </div> </div>`,TEMPLATES[`border-wrapper-mini-map`]=`<div class="border-wrapper-mini-map"></div>`,TEMPLATES[`element-mini-map`]=`<div class="element-m
```
### 12
```js
backlight=`<div class="depo_backlight"></div>`,TEMPLATES[`depo-filter`]=`<div class="depo-filter">     <div class="menu-wrapper">         <div class="menu"></div>     </div>     <div class="back"></div> </div>`,TEMPLATES[`mini-map-local-content`]=`<div class="mini-map-local-content">     <div class="graphic interface-element-middle-1-background-stretch"></div>     <div class="scroll-wrapper">         <div class="scroll-pane"></div>     </div> </div>`,TEMPLATES[`border-wrapper-mini-map`]=`<div class="border-wrapper-mini-map"></div>`,TEMPLATES[`element-mini-map`]=`<div class="element-mini-map element">     <div class="bord
```
### 13
```js
`mini-map-local-content`]=`<div class="mini-map-local-content">     <div class="graphic interface-element-middle-1-background-stretch"></div>     <div class="scroll-wrapper">         <div class="scroll-pane"></div>     </div> </div>`,TEMPLATES[`border-wrapper-mini-map`]=`<div class="border-wrapper-mini-map"></div>`,TEMPLATES[`element-mini-map`]=`<div class="element-mini-map element">     <div class="border-wrapper"></div> </div>`,TEMPLATES[`icon-wrapper-map`]=`<div class="icon-wrapper-map icon-wrapper">     <div class="emo-npc-icon"></div> </div>`,TEMPLATES[`one-location-on-map`]=`<div class="one-location-on-map"></div>`
```
### 14
```js
mini-map-local-content">     <div class="graphic interface-element-middle-1-background-stretch"></div>     <div class="scroll-wrapper">         <div class="scroll-pane"></div>     </div> </div>`,TEMPLATES[`border-wrapper-mini-map`]=`<div class="border-wrapper-mini-map"></div>`,TEMPLATES[`element-mini-map`]=`<div class="element-mini-map element">     <div class="border-wrapper"></div> </div>`,TEMPLATES[`icon-wrapper-map`]=`<div class="icon-wrapper-map icon-wrapper">     <div class="emo-npc-icon"></div> </div>`,TEMPLATES[`one-location-on-map`]=`<div class="one-location-on-map"></div>`,TEMPLATES[`search-wrapper`]=`<div clas
```
### 15
```js
ss="graphic interface-element-middle-1-background-stretch"></div>     <div class="scroll-wrapper">         <div class="scroll-pane"></div>     </div> </div>`,TEMPLATES[`border-wrapper-mini-map`]=`<div class="border-wrapper-mini-map"></div>`,TEMPLATES[`element-mini-map`]=`<div class="element-mini-map element">     <div class="border-wrapper"></div> </div>`,TEMPLATES[`icon-wrapper-map`]=`<div class="icon-wrapper-map icon-wrapper">     <div class="emo-npc-icon"></div> </div>`,TEMPLATES[`one-location-on-map`]=`<div class="one-location-on-map"></div>`,TEMPLATES[`search-wrapper`]=`<div class="search-wrapper">         <input cl
```
### 16
```js
ddle-1-background-stretch"></div>     <div class="scroll-wrapper">         <div class="scroll-pane"></div>     </div> </div>`,TEMPLATES[`border-wrapper-mini-map`]=`<div class="border-wrapper-mini-map"></div>`,TEMPLATES[`element-mini-map`]=`<div class="element-mini-map element">     <div class="border-wrapper"></div> </div>`,TEMPLATES[`icon-wrapper-map`]=`<div class="icon-wrapper-map icon-wrapper">     <div class="emo-npc-icon"></div> </div>`,TEMPLATES[`one-location-on-map`]=`<div class="one-location-on-map"></div>`,TEMPLATES[`search-wrapper`]=`<div class="search-wrapper">         <input class="search"/>         <div clas
```
### 17
```js
div>`,TEMPLATES[`one-location-on-map`]=`<div class="one-location-on-map"></div>`,TEMPLATES[`search-wrapper`]=`<div class="search-wrapper">         <input class="search"/>         <div class="search-x" data-trans="data-tip#delete"></div>     </div>`,TEMPLATES[`mini-map-global-content`]=`<div class="mini-map-global-content">     <div class="graphic interface-element-middle-1-background-stretch"></div>     <div class="scroll-wrapper classic-bar">         <div class="scroll-pane"></div>     </div> </div>`,TEMPLATES[`local-map-element`]=`<div class="local-map-element">     <div class="table-wrapper">         <div class="left-
```
### 18
```js
`<div class="one-location-on-map"></div>`,TEMPLATES[`search-wrapper`]=`<div class="search-wrapper">         <input class="search"/>         <div class="search-x" data-trans="data-tip#delete"></div>     </div>`,TEMPLATES[`mini-map-global-content`]=`<div class="mini-map-global-content">     <div class="graphic interface-element-middle-1-background-stretch"></div>     <div class="scroll-wrapper classic-bar">         <div class="scroll-pane"></div>     </div> </div>`,TEMPLATES[`local-map-element`]=`<div class="local-map-element">     <div class="table-wrapper">         <div class="left-side">             <div class="label"><
```
### 19
```js
</div>             <div class="toggle"></div>         </div>         <div class="icon-wrapper">             <div class="emo-npc-icon"></div>         </div>     </div>     <div class="line interface-element-line-1-background"></div> </div>`,TEMPLATES[`handheld-mini-map`]=`<div class="handheld-mini-map">        <canvas class="handheld-mini-map-canvas" ></canvas>    </div>`,TEMPLATES[`dynamic-bck`]=`<div class="dynamic-bck bck"></div>`,TEMPLATES[`show-monsters-header`]=`<div class="show-monsters-header"></div>`,TEMPLATES[`color-label-window-map`]=`<div class="color-label-window-map color-label"></div>`,TEMPLATES[`show-label
```
### 20
```js
ggle"></div>         </div>         <div class="icon-wrapper">             <div class="emo-npc-icon"></div>         </div>     </div>     <div class="line interface-element-line-1-background"></div> </div>`,TEMPLATES[`handheld-mini-map`]=`<div class="handheld-mini-map">        <canvas class="handheld-mini-map-canvas" ></canvas>    </div>`,TEMPLATES[`dynamic-bck`]=`<div class="dynamic-bck bck"></div>`,TEMPLATES[`show-monsters-header`]=`<div class="show-monsters-header"></div>`,TEMPLATES[`color-label-window-map`]=`<div class="color-label-window-map color-label"></div>`,TEMPLATES[`show-label-window-map`]=`<div class="show-l
```
### 21
```js
lass="icon-wrapper">             <div class="emo-npc-icon"></div>         </div>     </div>     <div class="line interface-element-line-1-background"></div> </div>`,TEMPLATES[`handheld-mini-map`]=`<div class="handheld-mini-map">        <canvas class="handheld-mini-map-canvas" ></canvas>    </div>`,TEMPLATES[`dynamic-bck`]=`<div class="dynamic-bck bck"></div>`,TEMPLATES[`show-monsters-header`]=`<div class="show-monsters-header"></div>`,TEMPLATES[`color-label-window-map`]=`<div class="color-label-window-map color-label"></div>`,TEMPLATES[`show-label-window-map`]=`<div class="show-label-window-map show-label"></div>`,TEMPLA
```
### 22
```js
show-label-data-drawer-prof-and-level show-label"></div>`,TEMPLATES[`show-label-who-is-here`]=`<div class="show-label-who-is-here show-label"></div>`,TEMPLATES[`show-label-map-blur`]=`<div class="show-label-map-blur show-label"></div>`,TEMPLATES[`icons-column-mini-map`]=`<div class="icons-column-mini-map icons-column mm-mark-list"></div>`,TEMPLATES[`first-column-mini-map`]=`<div class="first-column-mini-map first-column"></div>`,TEMPLATES[`second-column-mini-map`]=`<div class="second-column-mini-map second-column"></div>`,TEMPLATES[`color-to-choose-mini-map`]=`<div class="color-to-choose-mini-map color-to-choose"></div>`
```
### 23
```js
 show-label"></div>`,TEMPLATES[`show-label-who-is-here`]=`<div class="show-label-who-is-here show-label"></div>`,TEMPLATES[`show-label-map-blur`]=`<div class="show-label-map-blur show-label"></div>`,TEMPLATES[`icons-column-mini-map`]=`<div class="icons-column-mini-map icons-column mm-mark-list"></div>`,TEMPLATES[`first-column-mini-map`]=`<div class="first-column-mini-map first-column"></div>`,TEMPLATES[`second-column-mini-map`]=`<div class="second-column-mini-map second-column"></div>`,TEMPLATES[`color-to-choose-mini-map`]=`<div class="color-to-choose-mini-map color-to-choose"></div>`,TEMPLATES[`mini-map-other`]=`<div cl
```
### 24
```js
="show-label-who-is-here show-label"></div>`,TEMPLATES[`show-label-map-blur`]=`<div class="show-label-map-blur show-label"></div>`,TEMPLATES[`icons-column-mini-map`]=`<div class="icons-column-mini-map icons-column mm-mark-list"></div>`,TEMPLATES[`first-column-mini-map`]=`<div class="first-column-mini-map first-column"></div>`,TEMPLATES[`second-column-mini-map`]=`<div class="second-column-mini-map second-column"></div>`,TEMPLATES[`color-to-choose-mini-map`]=`<div class="color-to-choose-mini-map color-to-choose"></div>`,TEMPLATES[`mini-map-other`]=`<div class="mini-map-other other mark"></div>`,TEMPLATES[`mini-map-gateway`
```
### 25
```js
</div>`,TEMPLATES[`show-label-map-blur`]=`<div class="show-label-map-blur show-label"></div>`,TEMPLATES[`icons-column-mini-map`]=`<div class="icons-column-mini-map icons-column mm-mark-list"></div>`,TEMPLATES[`first-column-mini-map`]=`<div class="first-column-mini-map first-column"></div>`,TEMPLATES[`second-column-mini-map`]=`<div class="second-column-mini-map second-column"></div>`,TEMPLATES[`color-to-choose-mini-map`]=`<div class="color-to-choose-mini-map color-to-choose"></div>`,TEMPLATES[`mini-map-other`]=`<div class="mini-map-other other mark"></div>`,TEMPLATES[`mini-map-gateway`]=`<div class="mini-map-gateway gatew
```
### 26
```js
ow-label-map-blur show-label"></div>`,TEMPLATES[`icons-column-mini-map`]=`<div class="icons-column-mini-map icons-column mm-mark-list"></div>`,TEMPLATES[`first-column-mini-map`]=`<div class="first-column-mini-map first-column"></div>`,TEMPLATES[`second-column-mini-map`]=`<div class="second-column-mini-map second-column"></div>`,TEMPLATES[`color-to-choose-mini-map`]=`<div class="color-to-choose-mini-map color-to-choose"></div>`,TEMPLATES[`mini-map-other`]=`<div class="mini-map-other other mark"></div>`,TEMPLATES[`mini-map-gateway`]=`<div class="mini-map-gateway gateway mark"></div>`,TEMPLATES[`mini-map-rip`]=`<div class="
```
### 27
```js
TEMPLATES[`icons-column-mini-map`]=`<div class="icons-column-mini-map icons-column mm-mark-list"></div>`,TEMPLATES[`first-column-mini-map`]=`<div class="first-column-mini-map first-column"></div>`,TEMPLATES[`second-column-mini-map`]=`<div class="second-column-mini-map second-column"></div>`,TEMPLATES[`color-to-choose-mini-map`]=`<div class="color-to-choose-mini-map color-to-choose"></div>`,TEMPLATES[`mini-map-other`]=`<div class="mini-map-other other mark"></div>`,TEMPLATES[`mini-map-gateway`]=`<div class="mini-map-gateway gateway mark"></div>`,TEMPLATES[`mini-map-rip`]=`<div class="mini-map-rip rip mark"></div>`,TEMPLAT
```
### 28
```js
n-mini-map icons-column mm-mark-list"></div>`,TEMPLATES[`first-column-mini-map`]=`<div class="first-column-mini-map first-column"></div>`,TEMPLATES[`second-column-mini-map`]=`<div class="second-column-mini-map second-column"></div>`,TEMPLATES[`color-to-choose-mini-map`]=`<div class="color-to-choose-mini-map color-to-choose"></div>`,TEMPLATES[`mini-map-other`]=`<div class="mini-map-other other mark"></div>`,TEMPLATES[`mini-map-gateway`]=`<div class="mini-map-gateway gateway mark"></div>`,TEMPLATES[`mini-map-rip`]=`<div class="mini-map-rip rip mark"></div>`,TEMPLATES[`mini-map-monster`]=`<div class="mini-map-monster monste
```
### 29
```js
div>`,TEMPLATES[`first-column-mini-map`]=`<div class="first-column-mini-map first-column"></div>`,TEMPLATES[`second-column-mini-map`]=`<div class="second-column-mini-map second-column"></div>`,TEMPLATES[`color-to-choose-mini-map`]=`<div class="color-to-choose-mini-map color-to-choose"></div>`,TEMPLATES[`mini-map-other`]=`<div class="mini-map-other other mark"></div>`,TEMPLATES[`mini-map-gateway`]=`<div class="mini-map-gateway gateway mark"></div>`,TEMPLATES[`mini-map-rip`]=`<div class="mini-map-rip rip mark"></div>`,TEMPLATES[`mini-map-monster`]=`<div class="mini-map-monster monster mark"></div>`,TEMPLATES[`mini-map-reco
```
### 30
```js
v class="first-column-mini-map first-column"></div>`,TEMPLATES[`second-column-mini-map`]=`<div class="second-column-mini-map second-column"></div>`,TEMPLATES[`color-to-choose-mini-map`]=`<div class="color-to-choose-mini-map color-to-choose"></div>`,TEMPLATES[`mini-map-other`]=`<div class="mini-map-other other mark"></div>`,TEMPLATES[`mini-map-gateway`]=`<div class="mini-map-gateway gateway mark"></div>`,TEMPLATES[`mini-map-rip`]=`<div class="mini-map-rip rip mark"></div>`,TEMPLATES[`mini-map-monster`]=`<div class="mini-map-monster monster mark"></div>`,TEMPLATES[`mini-map-recovery`]=`<div class="mini-map-recovery recover
```
### 31
```js
 first-column"></div>`,TEMPLATES[`second-column-mini-map`]=`<div class="second-column-mini-map second-column"></div>`,TEMPLATES[`color-to-choose-mini-map`]=`<div class="color-to-choose-mini-map color-to-choose"></div>`,TEMPLATES[`mini-map-other`]=`<div class="mini-map-other other mark"></div>`,TEMPLATES[`mini-map-gateway`]=`<div class="mini-map-gateway gateway mark"></div>`,TEMPLATES[`mini-map-rip`]=`<div class="mini-map-rip rip mark"></div>`,TEMPLATES[`mini-map-monster`]=`<div class="mini-map-monster monster mark"></div>`,TEMPLATES[`mini-map-recovery`]=`<div class="mini-map-recovery recovery mark"></div>`,TEMPLATES[`her
```
### 32
```js
n-mini-map`]=`<div class="second-column-mini-map second-column"></div>`,TEMPLATES[`color-to-choose-mini-map`]=`<div class="color-to-choose-mini-map color-to-choose"></div>`,TEMPLATES[`mini-map-other`]=`<div class="mini-map-other other mark"></div>`,TEMPLATES[`mini-map-gateway`]=`<div class="mini-map-gateway gateway mark"></div>`,TEMPLATES[`mini-map-rip`]=`<div class="mini-map-rip rip mark"></div>`,TEMPLATES[`mini-map-monster`]=`<div class="mini-map-monster monster mark"></div>`,TEMPLATES[`mini-map-recovery`]=`<div class="mini-map-recovery recovery mark"></div>`,TEMPLATES[`hero-mark`]=`<div class="hero-mark mark"></div>`,
```
### 33
```js
-column-mini-map second-column"></div>`,TEMPLATES[`color-to-choose-mini-map`]=`<div class="color-to-choose-mini-map color-to-choose"></div>`,TEMPLATES[`mini-map-other`]=`<div class="mini-map-other other mark"></div>`,TEMPLATES[`mini-map-gateway`]=`<div class="mini-map-gateway gateway mark"></div>`,TEMPLATES[`mini-map-rip`]=`<div class="mini-map-rip rip mark"></div>`,TEMPLATES[`mini-map-monster`]=`<div class="mini-map-monster monster mark"></div>`,TEMPLATES[`mini-map-recovery`]=`<div class="mini-map-recovery recovery mark"></div>`,TEMPLATES[`hero-mark`]=`<div class="hero-mark mark"></div>`,TEMPLATES[`border-war-shadow`]=`
```
### 34
```js
`color-to-choose-mini-map`]=`<div class="color-to-choose-mini-map color-to-choose"></div>`,TEMPLATES[`mini-map-other`]=`<div class="mini-map-other other mark"></div>`,TEMPLATES[`mini-map-gateway`]=`<div class="mini-map-gateway gateway mark"></div>`,TEMPLATES[`mini-map-rip`]=`<div class="mini-map-rip rip mark"></div>`,TEMPLATES[`mini-map-monster`]=`<div class="mini-map-monster monster mark"></div>`,TEMPLATES[`mini-map-recovery`]=`<div class="mini-map-recovery recovery mark"></div>`,TEMPLATES[`hero-mark`]=`<div class="hero-mark mark"></div>`,TEMPLATES[`border-war-shadow`]=`<div class="border-war-shadow"></div>`,TEMPLATES[`
```
### 35
```js
`<div class="color-to-choose-mini-map color-to-choose"></div>`,TEMPLATES[`mini-map-other`]=`<div class="mini-map-other other mark"></div>`,TEMPLATES[`mini-map-gateway`]=`<div class="mini-map-gateway gateway mark"></div>`,TEMPLATES[`mini-map-rip`]=`<div class="mini-map-rip rip mark"></div>`,TEMPLATES[`mini-map-monster`]=`<div class="mini-map-monster monster mark"></div>`,TEMPLATES[`mini-map-recovery`]=`<div class="mini-map-recovery recovery mark"></div>`,TEMPLATES[`hero-mark`]=`<div class="hero-mark mark"></div>`,TEMPLATES[`border-war-shadow`]=`<div class="border-war-shadow"></div>`,TEMPLATES[`event-calendar`]=`<div class
```
### 36
```js
r-to-choose"></div>`,TEMPLATES[`mini-map-other`]=`<div class="mini-map-other other mark"></div>`,TEMPLATES[`mini-map-gateway`]=`<div class="mini-map-gateway gateway mark"></div>`,TEMPLATES[`mini-map-rip`]=`<div class="mini-map-rip rip mark"></div>`,TEMPLATES[`mini-map-monster`]=`<div class="mini-map-monster monster mark"></div>`,TEMPLATES[`mini-map-recovery`]=`<div class="mini-map-recovery recovery mark"></div>`,TEMPLATES[`hero-mark`]=`<div class="hero-mark mark"></div>`,TEMPLATES[`border-war-shadow`]=`<div class="border-war-shadow"></div>`,TEMPLATES[`event-calendar`]=`<div class="event-calendar">     <div class="backgro
```
### 37
```js
mini-map-other`]=`<div class="mini-map-other other mark"></div>`,TEMPLATES[`mini-map-gateway`]=`<div class="mini-map-gateway gateway mark"></div>`,TEMPLATES[`mini-map-rip`]=`<div class="mini-map-rip rip mark"></div>`,TEMPLATES[`mini-map-monster`]=`<div class="mini-map-monster monster mark"></div>`,TEMPLATES[`mini-map-recovery`]=`<div class="mini-map-recovery recovery mark"></div>`,TEMPLATES[`hero-mark`]=`<div class="hero-mark mark"></div>`,TEMPLATES[`border-war-shadow`]=`<div class="border-war-shadow"></div>`,TEMPLATES[`event-calendar`]=`<div class="event-calendar">     <div class="background">         <div class="matrix
```
### 38
```js
 mark"></div>`,TEMPLATES[`mini-map-gateway`]=`<div class="mini-map-gateway gateway mark"></div>`,TEMPLATES[`mini-map-rip`]=`<div class="mini-map-rip rip mark"></div>`,TEMPLATES[`mini-map-monster`]=`<div class="mini-map-monster monster mark"></div>`,TEMPLATES[`mini-map-recovery`]=`<div class="mini-map-recovery recovery mark"></div>`,TEMPLATES[`hero-mark`]=`<div class="hero-mark mark"></div>`,TEMPLATES[`border-war-shadow`]=`<div class="border-war-shadow"></div>`,TEMPLATES[`event-calendar`]=`<div class="event-calendar">     <div class="background">         <div class="matrix">             <div class="event-calendar-cell pre
```
### 39
```js
p-gateway`]=`<div class="mini-map-gateway gateway mark"></div>`,TEMPLATES[`mini-map-rip`]=`<div class="mini-map-rip rip mark"></div>`,TEMPLATES[`mini-map-monster`]=`<div class="mini-map-monster monster mark"></div>`,TEMPLATES[`mini-map-recovery`]=`<div class="mini-map-recovery recovery mark"></div>`,TEMPLATES[`hero-mark`]=`<div class="hero-mark mark"></div>`,TEMPLATES[`border-war-shadow`]=`<div class="border-war-shadow"></div>`,TEMPLATES[`event-calendar`]=`<div class="event-calendar">     <div class="background">         <div class="matrix">             <div class="event-calendar-cell prev-week week-switch"></div>       
```
### 40
```js
   <!--</div>--> </div>`,TEMPLATES[`divide-and-color-record`]=`<div class="divide-and-color-record">     <div class="txt-wrapper"><div class="text"></div></div>     <!--<div class="menu-wrapper"><div class="menu"></div></div>-->     <div class="show-hand-held-mini-map-checkbox-wrapper"></div>     <div class="show-data-drawer-nick-checkbox-wrapper"></div>     <div class="show-data-drawer-prof-and-level-checkbox-wrapper"></div>     <div class="show-who-is-here-checkbox-wrapper"></div>     <div class="show-map-blur-checkbox-wrapper"></div>     <div class="choose-color-wrapper"></div>     <div class="pick-color"></div> </div
```
_Only first 40 of 70 matches shown._

## inventory
Matches: **31**

### 1
```js
     <span data-trans="#no_leg_bon" class="nolegbon-tmp"></span>         <div class="bonuses"></div>     </div> </div>`,TEMPLATES[`interface-element-equipment-with-additional-bag`]=`<div class="interface-element-equipment-with-additional-bag">     <div class="equipment-wrapper-outline">         <div class="equipment-outline-1 equipment-outline"></div>         <div class="equipment-outline-2 equipment-outline"></div>         <div class="equipment-outline-3 equipment-outline"></div>         <div class="equipment-outline-4 equipment-outline"></div>     </div>     <div class="eq-slot" data-st="10"></div>     <div class="eq-slot inter
```
### 2
```js
iv class="eq-cl"></div></div>     <div class="eq-slot interface-element-one-item-slot-background-to-repeat" data-st="9"><div class="eq-cl"></div></div> </div>`,TEMPLATES[`interface-element-equipment`]=`<div class="interface-element-equipment">     <div class="equipment-wrapper-outline">         <div class="equipment-outline-1 equipment-outline"></div>         <div class="equipment-outline-2 equipment-outline"></div>         <div class="equipment-outline-3 equipment-outline"></div>         <div class="equipment-outline-4 equipment-outline"></div>     </div>     <div class="eq-slot" data-st="10"></div>     <div class="eq-slot inter
```
### 3
```js
class="stat blue js-res-frost"></span> /                             <span class="stat green js-res-poison"></span> %                         </span>                     </span>                 </li>             </ul>         </div>     </div>     <div class="equipment-wrapper">     </div>     <div class="builds-interface">         <div class="choose-build build-index"></div>     </div> <!--        <div class="lagmeter-light-mode">--> <!--            <div class="lag-val">0</div>--> <!--            <div class="lag">--> <!--                <div class="one-lag lag-5"></div>--> <!--                <div class="one-lag lag-4"></div>-->
```
### 4
```js
one-lag lag-3"></div>--> <!--                <div class="one-lag lag-2"></div>--> <!--                <div class="one-lag lag-1"></div>--> <!--                <div class="one-lag lag-0"></div>--> <!--            </div>--> <!--        </div>-->     <div class="stats-wrapper interface-element-background-color-3 interface-element-box-shadow-2 interface-element-grid-border">         <div class="header-title-wrapper">             <div class="interface-element-active-card-background-stretch"></div>             <div class="header-title" data-trans="#stats-head-title#stats"></div>         </div>         <div class="stats-button"></di
```
### 5
```js
div>`,TEMPLATES.stat=`<span class="stat"></span>`,TEMPLATES[`battle-set-wrapper`]=`<div class="battle-set-wrapper">     <div class="battle-set-choice"></div>     <div class="battle-set-choice"></div>     <div class="battle-set-choice"></div> </div>`,TEMPLATES.inventory_wrapper=`<div class="inventory_wrapper">     <div class="bags-navigation-bg interface-element-grid-border">         <div class="interface-element-one-black-tile bag-1 bag-slot-wrapper"><div class="interface-element-bag-eq-icon-background"></div></div>         <div class="interface-element-one-black-tile bag-2 bag-slot-wrapper"><div class="interface-element-bag-eq-i
```
### 6
```js
ss="stat"></span>`,TEMPLATES[`battle-set-wrapper`]=`<div class="battle-set-wrapper">     <div class="battle-set-choice"></div>     <div class="battle-set-choice"></div>     <div class="battle-set-choice"></div> </div>`,TEMPLATES.inventory_wrapper=`<div class="inventory_wrapper">     <div class="bags-navigation-bg interface-element-grid-border">         <div class="interface-element-one-black-tile bag-1 bag-slot-wrapper"><div class="interface-element-bag-eq-icon-background"></div></div>         <div class="interface-element-one-black-tile bag-2 bag-slot-wrapper"><div class="interface-element-bag-eq-icon-background"></div></div>   
```
### 7
```js
<div class="bag-2-slot" data-trans="data-tip#bag_space"></div>             <div class="bag-3-slot" data-trans="data-tip#bag_space"></div>             <div class="bag-4-slot" data-trans="data-tip#keys_bag_space"></div>         </div>     </div>     <div class="inventory-grid-bg interface-element-grid-border">         <div class="interface-element-item-slot-grid-stretch"></div>         <div class="inventory-grid">             <div class="inner-grid">                 <div class="scroll-pane"></div>             </div>         </div>     </div> </div>`,TEMPLATES.b_wrapper=`<div class="b_wrapper">     <div class="all-b"></div>     <
```
### 8
```js
           <div class="bag-4-slot" data-trans="data-tip#keys_bag_space"></div>         </div>     </div>     <div class="inventory-grid-bg interface-element-grid-border">         <div class="interface-element-item-slot-grid-stretch"></div>         <div class="inventory-grid">             <div class="inner-grid">                 <div class="scroll-pane"></div>             </div>         </div>     </div> </div>`,TEMPLATES.b_wrapper=`<div class="b_wrapper">     <div class="all-b"></div>     <div class="left"></div>     <div class="right"></div> </div>`,TEMPLATES[`captcha-pre-info`]=`<div class="captcha-pre-info">     <span data-
```
### 9
```js
attach-battle-hot-skills-help-window"></div>         <div class="surrender"></div>         <div class="left-column">             <div class="scroll-wrapper">                 <div class="scroll-pane"></div>             </div>         </div>         <div class="stats-wrapper"></div>         <div class="buffs-wrapper"></div>         <div class="buttons-wrapper"></div>         <div class="right-column">             <div class="scroll-wrapper">                 <div class="scroll-pane">                     <div class="turn-prediction"></div>                 </div>             </div>             <div class="battle-end-layer" data-tr
```
### 10
```js
aphic"></div>-->         <div class="requirements-wrapper stone interface-element-active-card-border-image">             <div class="title" data-trans="#lower_requirements#skills"></div>             <div class="icons"></div>         </div>         <div class="stats-wrapper stone interface-element-active-card-border-image">             <div class="stats-h" data-trans="#stats_header#skills"></div>             <div class="icon-tip" data-trans="data-tip#next_level_stat_info#buttons"></div>             <div class="all-stats"></div>         </div>     </div> </div>`,TEMPLATES[`skills-description-wrapper`]=`<div class="info-box skil
```
### 11
```js
))},this.getActiveBag=()=>r,this.useOrEquipItem=t=>{n.soulboundAlert(t)||n.blockBadTutorialItem(t)||n.checkBlessEquipped(t)||n.sendUseRequest(t)},this.init=function(){let t=Engine.interface.getRightMainColumnWrapper();b=t.find(`.character_wrapper`),y=t.find(`.inventory_wrapper`),x=t.find(`.bags-navigation`),C=getEngine().interface.get$interfaceLayer().find(`.inventory_wrapper`).find(`.scroll-pane`),this.initBeforeUpdateItems(),this.initAfterUpdateItems(),Engine.items.fetch(Engine.itemsFetchData.NEW_INVENTORY_ITEM,n.newInventoryItems),b.find(`.equipment-wrapper`).droppable({accept:`.item:not(.shop-item)`,drop:function(t,r){var i=r
```
### 12
```js
.checkBlessEquipped(t)||n.sendUseRequest(t)},this.init=function(){let t=Engine.interface.getRightMainColumnWrapper();b=t.find(`.character_wrapper`),y=t.find(`.inventory_wrapper`),x=t.find(`.bags-navigation`),C=getEngine().interface.get$interfaceLayer().find(`.inventory_wrapper`).find(`.scroll-pane`),this.initBeforeUpdateItems(),this.initAfterUpdateItems(),Engine.items.fetch(Engine.itemsFetchData.NEW_INVENTORY_ITEM,n.newInventoryItems),b.find(`.equipment-wrapper`).droppable({accept:`.item:not(.shop-item)`,drop:function(t,r){var i=r.draggable.data(`item`);if(!(Engine.dead&&!i.issetReviveStat())){var a=Math.floor((r.offset.left-$(th
```
### 13
```js
`.bags-navigation`),C=getEngine().interface.get$interfaceLayer().find(`.inventory_wrapper`).find(`.scroll-pane`),this.initBeforeUpdateItems(),this.initAfterUpdateItems(),Engine.items.fetch(Engine.itemsFetchData.NEW_INVENTORY_ITEM,n.newInventoryItems),b.find(`.equipment-wrapper`).droppable({accept:`.item:not(.shop-item)`,drop:function(t,r){var i=r.draggable.data(`item`);if(!(Engine.dead&&!i.issetReviveStat())){var a=Math.floor((r.offset.left-$(this).offset().left+r.draggable.width()*Engine.zoomFactor/2)/33/Engine.zoomFactor),s=Math.floor((r.offset.top-$(this).offset().top+r.draggable.height()*Engine.zoomFactor/2)/33/Engine.zoomFac
```
### 14
```js
uipItem(i):message(_t(`need__lvl`,{"%val%":25}));else{let t=`moveitem&st=9&id=`+i.id,r=Engine.heroEquipment.getItemBySt(ItemData_default.ST.PURSE);if(ItemState.isEquippedSt(i.st)&&!ItemState.isPurseSt(i.st)&&r&&n.soulboundAlert(r,t))return;_g(t)}}}}),y.find(`.inventory-grid`).droppable({accept:`.item:not(.shop-item)`,drop:function(t,i){turboDevHelper.resolve(`EQ_ITEM_DRAGGING_DROP`,{e:t,ui:i});let a=6,s=0,c=i.draggable.data(`item`);if(i.draggable.hasClass(`bottomItem`)){Engine.interfaceItems.deleteExistItem(c.id,c);return}var l=$(this).offset(),u=Math.floor((i.offset.top-l.top+i.draggable.height()*Engine.zoomFactor/2)/33/Engin
```
### 15
```js
ault.get(`stasis-incoming-overlay`)),p.append(Templates_default.get(`stasis-overlay`)),p.append(Templates_default.get(`map-reloader-splash`)),p.append(Templates_default.get(`dead-overlay`)),F=Templates_default.get(`character_wrapper`),P=Templates_default.get(`inventory_wrapper`);let l=Templates_default.get(`interface-element-equipment-with-additional-bag`).addClass(`equipment-wrapper`);F.find(`.equipment-wrapper`).replaceWith(l);let u=Ie();u.append(F),u.append(Templates_default.get(`battle-set-wrapper`)),u.append(P),u.append($(`<div>`).addClass(`tutorial-banner-anchor`))};let Ie=()=>f.find(`.right-column`).find(`.inner-wrapper`).
```
### 16
```js
ault.get(`map-reloader-splash`)),p.append(Templates_default.get(`dead-overlay`)),F=Templates_default.get(`character_wrapper`),P=Templates_default.get(`inventory_wrapper`);let l=Templates_default.get(`interface-element-equipment-with-additional-bag`).addClass(`equipment-wrapper`);F.find(`.equipment-wrapper`).replaceWith(l);let u=Ie();u.append(F),u.append(Templates_default.get(`battle-set-wrapper`)),u.append(P),u.append($(`<div>`).addClass(`tutorial-banner-anchor`))};let Ie=()=>f.find(`.right-column`).find(`.inner-wrapper`).find(`.right-main-column-wrapper`);this.clearCanvasCursor=()=>{let t=ColliderData_default.CURSOR;h.removeClas
```
### 17
```js
`)),p.append(Templates_default.get(`dead-overlay`)),F=Templates_default.get(`character_wrapper`),P=Templates_default.get(`inventory_wrapper`);let l=Templates_default.get(`interface-element-equipment-with-additional-bag`).addClass(`equipment-wrapper`);F.find(`.equipment-wrapper`).replaceWith(l);let u=Ie();u.append(F),u.append(Templates_default.get(`battle-set-wrapper`)),u.append(P),u.append($(`<div>`).addClass(`tutorial-banner-anchor`))};let Ie=()=>f.find(`.right-column`).find(`.inner-wrapper`).find(`.right-main-column-wrapper`);this.clearCanvasCursor=()=>{let t=ColliderData_default.CURSOR;h.removeClass(`${t.DO_ACTION} ${t.PICK_UP
```
### 18
```js
][1])},this.sendGA=(t,n,r)=>{Engine.worldConfig.getWorldName()!==`dev`&&Engine.GA.send(t,n,r)},this.addStaticButtons=function(){I=new Button({text:Qe(!1),classes:[`stats-expand`,`small`,`green`],action:()=>{this.clickMoreBtn()}}),t.get$interfaceLayer().find(`.stats-wrapper`).find(`.stats-button`).append(I.getButton()),L=new Button({text:Qe(!1),classes:[`stats-expand`,`small`,`green`],action:()=>{this.clickMoreBtn()}}),t.get$interfaceLayer().find(`.stats-light-mode`).find(`.stats-button`).append(L.getButton()),Engine.hotKeys.replaceshowhideStatsBtnsNames(),isset(Engine.hero.previewAcc)&&isEn()&&$e(),t.initPvpButton()},this.reg
```
### 19
```js
ni_mobile_pl`,headerPc:`t_header_3_ni_pl`,headerMobile:`t_header_3_ni_pl`,graphic:`/img/gui/newTutorial/4.gif`,htmlFocus:`.interface-layer>.right-column.main-column`,htmlPosition:`.interface-layer>.right-column.main-column`,htmlMultiGlow:[`.character_wrapper>.equipment-wrapper>[data-st=5]`,`.character_wrapper>.equipment-wrapper>[data-st=7]`],blink:!0,idMaps:[1456],itemsNeed:{htmlMultiGlow:!0,items:{[ProfData_default.WARRIOR]:{1:{loc:`g`,tpl:10446},14:{loc:`g`,tpl:10447}},[ProfData_default.PALADIN]:{1:{loc:`g`},14:{loc:`g`}},[ProfData_default.MAGE]:{6:{loc:`g`},7:{loc:`g`}},[ProfData_default.TRACKER]:{4:{loc:`g`},29:{loc:`g`}},[Pr
```
### 20
```js
le:`t_header_3_ni_pl`,graphic:`/img/gui/newTutorial/4.gif`,htmlFocus:`.interface-layer>.right-column.main-column`,htmlPosition:`.interface-layer>.right-column.main-column`,htmlMultiGlow:[`.character_wrapper>.equipment-wrapper>[data-st=5]`,`.character_wrapper>.equipment-wrapper>[data-st=7]`],blink:!0,idMaps:[1456],itemsNeed:{htmlMultiGlow:!0,items:{[ProfData_default.WARRIOR]:{1:{loc:`g`,tpl:10446},14:{loc:`g`,tpl:10447}},[ProfData_default.PALADIN]:{1:{loc:`g`},14:{loc:`g`}},[ProfData_default.MAGE]:{6:{loc:`g`},7:{loc:`g`}},[ProfData_default.TRACKER]:{4:{loc:`g`},29:{loc:`g`}},[ProfData_default.HUNTER]:{4:{loc:`g`},29:{loc:`g`}},[P
```
### 21
```js
tObserve(),blink:!0}],11:[{textPc:`t_11_ni_pl`,textMobile:`t_11_ni_mobile_pl`,headerPc:`t_header_11_ni_pl`,headerMobile:`t_header_11_ni_pl`,graphic:`/img/gui/newTutorial/4.gif`,idMaps:[707],htmlFocus:`.interface-layer>.right-column.main-column`,htmlPosition:`.inventory_wrapper>.inventory-grid-bg`,itemsNeed:{htmlMultiGlow:!0,items:{[ProfData_default.WARRIOR]:{16:{loc:`g`,tpl:25356}},[ProfData_default.PALADIN]:{16:{loc:`g`,tpl:25356}},[ProfData_default.MAGE]:{16:{loc:`g`,tpl:25356}},[ProfData_default.TRACKER]:{16:{loc:`g`,tpl:25356}},[ProfData_default.HUNTER]:{16:{loc:`g`,tpl:25356}},[ProfData_default.BLADE_DANCER]:{16:{loc:`g`,tpl
```
### 22
```js
}],11:[{textPc:`t_11_ni_pl`,textMobile:`t_11_ni_mobile_pl`,headerPc:`t_header_11_ni_pl`,headerMobile:`t_header_11_ni_pl`,graphic:`/img/gui/newTutorial/4.gif`,idMaps:[707],htmlFocus:`.interface-layer>.right-column.main-column`,htmlPosition:`.inventory_wrapper>.inventory-grid-bg`,itemsNeed:{htmlMultiGlow:!0,items:{[ProfData_default.WARRIOR]:{16:{loc:`g`,tpl:25356}},[ProfData_default.PALADIN]:{16:{loc:`g`,tpl:25356}},[ProfData_default.MAGE]:{16:{loc:`g`,tpl:25356}},[ProfData_default.TRACKER]:{16:{loc:`g`,tpl:25356}},[ProfData_default.HUNTER]:{16:{loc:`g`,tpl:25356}},[ProfData_default.BLADE_DANCER]:{16:{loc:`g`,tpl:25356}}}},blink
```
### 23
```js
header_13_ni_pl`,headerMobile:`t_header_13_ni_pl`,graphic:`/img/gui/newTutorial/4.gif`,idMaps:[707],maxLevel:7,htmlFocus:`.interface-layer>.right-column.main-column`,htmlPosition:`.interface-layer>.right-column.main-column`,htmlMultiGlow:[`.character_wrapper>.equipment-wrapper>[data-st=1]`],itemsNeed:{htmlMultiGlow:!0,items:{[ProfData_default.WARRIOR]:{9:{loc:`g`,tpl:65}},[ProfData_default.PALADIN]:{9:{loc:`g`,tpl:65}},[ProfData_default.MAGE]:{9:{loc:`g`,tpl:65}},[ProfData_default.TRACKER]:{9:{loc:`g`,tpl:65}},[ProfData_default.HUNTER]:{9:{loc:`g`,tpl:65}},[ProfData_default.BLADE_DANCER]:{9:{loc:`g`,tpl:65}}},minOneOfAllNotEquip:
```
### 24
```js
},[ProfData_default.HUNTER]:{24:{loc:`g`,tpl:25364}},[ProfData_default.BLADE_DANCER]:{24:{loc:`g`,tpl:25364}}},minOneOfAllNotEquip:!0},graphic:`/img/gui/newTutorial/12.gif`,htmlMultiGlow:[`.game-window-positioner>.interface-layer>.right-column>.inner-wrapper>.inventory_wrapper>.bags-navigation>.tutorial-bag`],htmlPosition:`.interface-layer>.right-column.main-column`,minLevel:10,maxLevel:20,idMaps:[707],blink:!0,blockedWidget:[i],blockedHotKeys:[n],additionalFunctionBeforeCreate:t.manageEqColumn}],34:[{textPc:`t_34_ni_pl`,textMobile:`t_34_ni_mobile_pl`,headerPc:`t_header_34_ni_pl`,headerMobile:`t_header_34_ni_pl`,mobileAddClass:s,
```
### 25
```js
obile_pl`,headerPc:`t_header_3_ni_pl`,headerMobile:`t_header_3_ni_pl`,graphic:`/img/gui/newTutorial/4_eng.gif`,htmlFocus:`.interface-layer>.right-column.main-column`,htmlPosition:`.interface-layer>.right-column.main-column`,htmlMultiGlow:[`.character_wrapper>.equipment-wrapper>[data-st=5]`,`.character_wrapper>.equipment-wrapper>[data-st=6]`,`.character_wrapper>.equipment-wrapper>[data-st=7]`],blink:!0,idMaps:[3877],itemsNeed:{htmlMultiGlow:!0,items:{[ProfData_default.WARRIOR]:{8:{loc:`g`},1:{loc:`g`},14:{loc:`g`}},[ProfData_default.PALADIN]:{8:{loc:`g`},1:{loc:`g`},14:{loc:`g`}},[ProfData_default.MAGE]:{8:{loc:`g`},6:{loc:`g`},5:
```
### 26
```js
t_header_3_ni_pl`,graphic:`/img/gui/newTutorial/4_eng.gif`,htmlFocus:`.interface-layer>.right-column.main-column`,htmlPosition:`.interface-layer>.right-column.main-column`,htmlMultiGlow:[`.character_wrapper>.equipment-wrapper>[data-st=5]`,`.character_wrapper>.equipment-wrapper>[data-st=6]`,`.character_wrapper>.equipment-wrapper>[data-st=7]`],blink:!0,idMaps:[3877],itemsNeed:{htmlMultiGlow:!0,items:{[ProfData_default.WARRIOR]:{8:{loc:`g`},1:{loc:`g`},14:{loc:`g`}},[ProfData_default.PALADIN]:{8:{loc:`g`},1:{loc:`g`},14:{loc:`g`}},[ProfData_default.MAGE]:{8:{loc:`g`},6:{loc:`g`},5:{loc:`g`}},[ProfData_default.TRACKER]:{8:{loc:`g`},4
```
### 27
```js
g.gif`,htmlFocus:`.interface-layer>.right-column.main-column`,htmlPosition:`.interface-layer>.right-column.main-column`,htmlMultiGlow:[`.character_wrapper>.equipment-wrapper>[data-st=5]`,`.character_wrapper>.equipment-wrapper>[data-st=6]`,`.character_wrapper>.equipment-wrapper>[data-st=7]`],blink:!0,idMaps:[3877],itemsNeed:{htmlMultiGlow:!0,items:{[ProfData_default.WARRIOR]:{8:{loc:`g`},1:{loc:`g`},14:{loc:`g`}},[ProfData_default.PALADIN]:{8:{loc:`g`},1:{loc:`g`},14:{loc:`g`}},[ProfData_default.MAGE]:{8:{loc:`g`},6:{loc:`g`},5:{loc:`g`}},[ProfData_default.TRACKER]:{8:{loc:`g`},4:{loc:`g`},21:{loc:`g`}},[ProfData_default.HUNTER]:{
```
### 28
```js
re9}],11:[{textPc:`t_11_ni_pl`,textMobile:`t_11_ni_mobile_pl`,headerPc:`t_header_11_ni_pl`,headerMobile:`t_header_11_ni_pl`,graphic:`/img/gui/newTutorial/4_eng.gif`,idMaps:[3877],minLevel:5,htmlFocus:`.interface-layer>.right-column.main-column`,htmlPosition:`.inventory_wrapper>.inventory-grid-bg`,itemsNeed:{htmlMultiGlow:!0,items:{[ProfData_default.WARRIOR]:{16:{loc:`g`}},[ProfData_default.PALADIN]:{16:{loc:`g`}},[ProfData_default.MAGE]:{16:{loc:`g`}},[ProfData_default.TRACKER]:{16:{loc:`g`}},[ProfData_default.HUNTER]:{16:{loc:`g`}},[ProfData_default.BLADE_DANCER]:{16:{loc:`g`}}},stats:{lootbox:!0,lvl:[TutorialData_default.STAT_O
```
### 29
```js
t_11_ni_pl`,textMobile:`t_11_ni_mobile_pl`,headerPc:`t_header_11_ni_pl`,headerMobile:`t_header_11_ni_pl`,graphic:`/img/gui/newTutorial/4_eng.gif`,idMaps:[3877],minLevel:5,htmlFocus:`.interface-layer>.right-column.main-column`,htmlPosition:`.inventory_wrapper>.inventory-grid-bg`,itemsNeed:{htmlMultiGlow:!0,items:{[ProfData_default.WARRIOR]:{16:{loc:`g`}},[ProfData_default.PALADIN]:{16:{loc:`g`}},[ProfData_default.MAGE]:{16:{loc:`g`}},[ProfData_default.TRACKER]:{16:{loc:`g`}},[ProfData_default.HUNTER]:{16:{loc:`g`}},[ProfData_default.BLADE_DANCER]:{16:{loc:`g`}}},stats:{lootbox:!0,lvl:[TutorialData_default.STAT_OPERATION.NUMBER_
```
### 30
```js
Pc:`t_header_13_ni_pl`,headerMobile:`t_header_13_ni_pl`,graphic:`/img/gui/newTutorial/4_eng.gif`,idMaps:[3877],htmlFocus:`.interface-layer>.right-column.main-column`,htmlPosition:`.interface-layer>.right-column.main-column`,htmlMultiGlow:[`.character_wrapper>.equipment-wrapper>[data-st=8]`],itemsNeed:{htmlMultiGlow:!0,items:{[ProfData_default.WARRIOR]:{10:{loc:`g`}},[ProfData_default.PALADIN]:{10:{loc:`g`}},[ProfData_default.MAGE]:{10:{loc:`g`}},[ProfData_default.TRACKER]:{10:{loc:`g`}},[ProfData_default.HUNTER]:{10:{loc:`g`}},[ProfData_default.BLADE_DANCER]:{10:{loc:`g`}}},minOneOfAllNotEquip:!0,stats:{lvl:[TutorialData_default.
```
### 31
```js
m`,`translateX(-50%)`),V=new BattlePredictionHelpWindow,V.init(),H=new BattleHotSkillsHelpWindow,H.init(),B=m[0].querySelector(`.turn-prediction`)},this.getFlist1=()=>w,this.getFlist2=()=>T,this.getTeamIDs=()=>r,this.initProgressBars=function(){var t=m.find(`.stats-wrapper`);this.createProgressBar(t,`hp-progress-bar red`),this.createProgressBar(t,`ep-progress-bar yellow`),this.createProgressBar(t,`mp-progress-bar blue`)},this.initObjects=function(){this.skillBattleMenu=new SkillBattleMenu,this.warriors=new Warriors,this.scaleBattle=new ScaleBattle,this.battleEffectsController=new BattleEffectsController,this.battleEffectsCont
```

## classlist
Matches: **223**

### 1
```js
efault:return!1}},errorReport$1=(t,n,r,i,a)=>{if(i=i||``,a){console.error(`[${t}, ${n}] ${r}`,i,a);return}console.error(`[${t}, ${n}] ${r}`,i)},throwError=(t,n,r)=>{throw Error(`[${t}, ${n}] ${r}`)},configIcon=()=>{let t=document.createElement(`div`);return t.classList.add(`add-bck`,`config`),t},siblings=t=>[...t.parentElement.children].filter(n=>n!==t),getAllProfName$1=t=>({m:_t(`prof_mag`,null,`eq_prof`),w:_t(`prof_warrior`,null,`eq_prof`),p:_t(`prof_paladyn`,null,`eq_prof`),t:_t(`prof_tracker`,null,`eq_prof`),h:_t(`prof_hunter`,null,`eq_prof`),b:_t(`prof_bladedancer`,null,`eq_prof`)})[t],removeFromArray$1=(t,n)=>{let r=t.i
```
### 2
```js
umber(n):n])),Icons=function(t){return t.CLOSE=`close`,t.MENU=`menu`,t.COPY=`copy`,t.LINK_EXTERNAL=`link-external`,t.ARROW_LEFT=`arrow-left`,t.ARROW_RIGHT=`arrow-right`,t.REFRESH=`refresh`,t}({}),getIcon=(t,n=!0)=>{let r=document.createElement(`div`);return r.classList.add(`ie-icon`,`ie-icon-${t}`),n||r.classList.add(`ie-icon--no-hover`),$(r)},getIconClose=t=>getIcon(`close`,t),highlightElement=(t,n=300)=>{document.querySelectorAll(t).forEach(t=>{t.classList.add(`ie-highlight-animation`),setTimeout(()=>{t.classList.remove(`ie-highlight-animation`)},2e3)})},attachItemToSlot=t=>{let{itemId:n,slotEl:r,viewName:i,movedName:a,clea
```
### 3
```js
E=`close`,t.MENU=`menu`,t.COPY=`copy`,t.LINK_EXTERNAL=`link-external`,t.ARROW_LEFT=`arrow-left`,t.ARROW_RIGHT=`arrow-right`,t.REFRESH=`refresh`,t}({}),getIcon=(t,n=!0)=>{let r=document.createElement(`div`);return r.classList.add(`ie-icon`,`ie-icon-${t}`),n||r.classList.add(`ie-icon--no-hover`),$(r)},getIconClose=t=>getIcon(`close`,t),highlightElement=(t,n=300)=>{document.querySelectorAll(t).forEach(t=>{t.classList.add(`ie-highlight-animation`),setTimeout(()=>{t.classList.remove(`ie-highlight-animation`)},2e3)})},attachItemToSlot=t=>{let{itemId:n,slotEl:r,viewName:i,movedName:a,clearSlotBeforeAppend:s=!0,correctItemCheck:c,con
```
### 4
```js
}),getIcon=(t,n=!0)=>{let r=document.createElement(`div`);return r.classList.add(`ie-icon`,`ie-icon-${t}`),n||r.classList.add(`ie-icon--no-hover`),$(r)},getIconClose=t=>getIcon(`close`,t),highlightElement=(t,n=300)=>{document.querySelectorAll(t).forEach(t=>{t.classList.add(`ie-highlight-animation`),setTimeout(()=>{t.classList.remove(`ie-highlight-animation`)},2e3)})},attachItemToSlot=t=>{let{itemId:n,slotEl:r,viewName:i,movedName:a,clearSlotBeforeAppend:s=!0,correctItemCheck:c,contextMenu:l,onClick:u,onDelete:f,onSuccess:p}=t,m=Engine.items.getItemById(n);if(!isset$4(m))return;if(c&&!c(m)){errorReport$1(`Helpers.ts`,`attachIt
```
### 5
```js
return r.classList.add(`ie-icon`,`ie-icon-${t}`),n||r.classList.add(`ie-icon--no-hover`),$(r)},getIconClose=t=>getIcon(`close`,t),highlightElement=(t,n=300)=>{document.querySelectorAll(t).forEach(t=>{t.classList.add(`ie-highlight-animation`),setTimeout(()=>{t.classList.remove(`ie-highlight-animation`)},2e3)})},attachItemToSlot=t=>{let{itemId:n,slotEl:r,viewName:i,movedName:a,clearSlotBeforeAppend:s=!0,correctItemCheck:c,contextMenu:l,onClick:u,onDelete:f,onSuccess:p}=t,m=Engine.items.getItemById(n);if(!isset$4(m))return;if(c&&!c(m)){errorReport$1(`Helpers.ts`,`attachItemToSlot`,`Incorrect item:`,m);return}let h=Engine.items.crea
```
### 6
```js
accept:r=_t(`yes`),cancel:i=_t(`no`)})=>{mAlert(t,[{txt:r,callback:()=>(typeof n==`function`&&n(),!0)},{txt:i,callback:()=>!0}])},createElement=(t,n)=>{let r=document.createElement(t);if(!n)return r;n.id&&(r.id=n.id),n.className&&(Array.isArray(n.className)?r.classList.add(...n.className):r.className=n.className),n.text&&(r.textContent=n.text),n.style&&Object.assign(r.style,n.style);let i=t=>{typeof t==`string`?r.appendChild(document.createTextNode(t)):r.appendChild(t)};return n.children&&(Array.isArray(n.children)?n.children.forEach(i):i(n.children)),n.attributes&&Object.entries(n.attributes).forEach(([t,n])=>{r.setAttribute
```
### 7
```js
ure().getTpl(...t),getEl:(...t)=>ensure().getEl(...t)},Button=class{constructor(t){this.disabled=!1,this.el=Templates_default.get(`button`)[0],this.createButton(t)}createButton({text:t,classes:n=[`small`,`green`],action:r,tip:i,disabled:a,attrs:s}){n&&this.el.classList.add(...n);let c=getClickEventName$1();this.el.addEventListener(c,t=>{r&&r(t,this.el)}),a&&this.setState(!0),i&&this.setTip(i),s&&setAttributes(this.el,s),this.setLabel(t)}setState(t){this.disabled=t,this.disabled?this.el.classList.add(`disable`):this.el.classList.remove(`disable`)}getState(){return this.disabled}setLabel(t){typeof t==`string`||t===void 0?this.e
```
### 8
```js
abled:a,attrs:s}){n&&this.el.classList.add(...n);let c=getClickEventName$1();this.el.addEventListener(c,t=>{r&&r(t,this.el)}),a&&this.setState(!0),i&&this.setTip(i),s&&setAttributes(this.el,s),this.setLabel(t)}setState(t){this.disabled=t,this.disabled?this.el.classList.add(`disable`):this.el.classList.remove(`disable`)}getState(){return this.disabled}setLabel(t){typeof t==`string`||t===void 0?this.el.querySelector(`.label`).innerText=t:this.el.querySelector(`.label`).appendChild(t)}setTip(t){return $(this.el).tip(t)}getButton(){return this.el}};function InputComponent(){let t=null,n=null,r=null,i=({val:i,cl:a,type:s,placehold
```
### 9
```js
sList.add(...n);let c=getClickEventName$1();this.el.addEventListener(c,t=>{r&&r(t,this.el)}),a&&this.setState(!0),i&&this.setTip(i),s&&setAttributes(this.el,s),this.setLabel(t)}setState(t){this.disabled=t,this.disabled?this.el.classList.add(`disable`):this.el.classList.remove(`disable`)}getState(){return this.disabled}setLabel(t){typeof t==`string`||t===void 0?this.el.querySelector(`.label`).innerText=t:this.el.querySelector(`.label`).appendChild(t)}setTip(t){return $(this.el).tip(t)}getButton(){return this.el}};function InputComponent(){let t=null,n=null,r=null,i=({val:i,cl:a,type:s,placeholder:c,changeClb:l,focusoutClb:u,mobil
```
### 10
```js
of t==`string`?t.charAt(0).toUpperCase()+t.slice(1):``,window.decapitalize=t=>typeof t==`string`?t.charAt(0).toLowerCase()+t.slice(1):``,window.removeSpaces=t=>t.replace(/\s/g,``),window.createButton=(t,n,r)=>{let i=Templates_default.get(`button`)[0];return i.classList.add(...n),i.querySelector(`.label`).innerHTML=t,i.addEventListener(getClickEventName$1(),r),i},window.createSmallButtonWithBackground=(t,n,r)=>{let i=Templates_default.get(`button`)[0],a=Templates_default.get(`add-bck`)[0];return i.append(a),i.classList.add(`small`),i.classList.add(`small-button-with-background`),i.classList.add(...n),a.classList.add(...t),i.ad
```
### 11
```js
urn i.classList.add(...n),i.querySelector(`.label`).innerHTML=t,i.addEventListener(getClickEventName$1(),r),i},window.createSmallButtonWithBackground=(t,n,r)=>{let i=Templates_default.get(`button`)[0],a=Templates_default.get(`add-bck`)[0];return i.append(a),i.classList.add(`small`),i.classList.add(`small-button-with-background`),i.classList.add(...n),a.classList.add(...t),i.addEventListener(`click`,r),i},window.setDebugMode=t=>{if(!elementIsArray(t)){errorReport$1(`Helpers.js`,`setDebugMode`,`debugKeysList is not array`,t);return}for(let n in CFG.DEBUG_KEYS)CFG.debug[n]=t.includes(n);afterDebugModeChanged();let n=`debug-mode-
```
### 12
```js
,i.querySelector(`.label`).innerHTML=t,i.addEventListener(getClickEventName$1(),r),i},window.createSmallButtonWithBackground=(t,n,r)=>{let i=Templates_default.get(`button`)[0],a=Templates_default.get(`add-bck`)[0];return i.append(a),i.classList.add(`small`),i.classList.add(`small-button-with-background`),i.classList.add(...n),a.classList.add(...t),i.addEventListener(`click`,r),i},window.setDebugMode=t=>{if(!elementIsArray(t)){errorReport$1(`Helpers.js`,`setDebugMode`,`debugKeysList is not array`,t);return}for(let n in CFG.DEBUG_KEYS)CFG.debug[n]=t.includes(n);afterDebugModeChanged();let n=`debug-mode-on`,r=$(`body`);CFG.debug
```
### 13
```js
tListener(getClickEventName$1(),r),i},window.createSmallButtonWithBackground=(t,n,r)=>{let i=Templates_default.get(`button`)[0],a=Templates_default.get(`add-bck`)[0];return i.append(a),i.classList.add(`small`),i.classList.add(`small-button-with-background`),i.classList.add(...n),a.classList.add(...t),i.addEventListener(`click`,r),i},window.setDebugMode=t=>{if(!elementIsArray(t)){errorReport$1(`Helpers.js`,`setDebugMode`,`debugKeysList is not array`,t);return}for(let n in CFG.DEBUG_KEYS)CFG.debug[n]=t.includes(n);afterDebugModeChanged();let n=`debug-mode-on`,r=$(`body`);CFG.debug[CFG.DEBUG_KEYS.MAIN]?r.addClass(n):r.removeClas
```
### 14
```js
tName$1(),r),i},window.createSmallButtonWithBackground=(t,n,r)=>{let i=Templates_default.get(`button`)[0],a=Templates_default.get(`add-bck`)[0];return i.append(a),i.classList.add(`small`),i.classList.add(`small-button-with-background`),i.classList.add(...n),a.classList.add(...t),i.addEventListener(`click`,r),i},window.setDebugMode=t=>{if(!elementIsArray(t)){errorReport$1(`Helpers.js`,`setDebugMode`,`debugKeysList is not array`,t);return}for(let n in CFG.DEBUG_KEYS)CFG.debug[n]=t.includes(n);afterDebugModeChanged();let n=`debug-mode-on`,r=$(`body`);CFG.debug[CFG.DEBUG_KEYS.MAIN]?r.addClass(n):r.removeClass(n)},window.getDebug=
```
### 15
```js
t.min,t.max]),this.options={...this.defaultOptions,...t},this.createElement(),this.setParameters()}createElement(){this.el=document.createElement(`div`),this.el.className=`c-slider`,this.input=document.createElement(`input`),this.input.type=`range`,this.input.classList.add(`c-slider__input`),this.stateEl=document.createElement(`div`),this.stateEl.classList.add(`c-slider__state`)}setParameters(){let{value:t,min:n,max:r,range:i,cssClass:a,tip:s,disabled:c,showValue:l,blockValueBelowCurrent:u,updateEvent:f,onUpdate:p}=this.options,[m,h]=i;this.el.classList.add(...a),this.setValue(t),this.setMin(n),this.setMax(r),this.setState(c)
```
### 16
```js
ameters()}createElement(){this.el=document.createElement(`div`),this.el.className=`c-slider`,this.input=document.createElement(`input`),this.input.type=`range`,this.input.classList.add(`c-slider__input`),this.stateEl=document.createElement(`div`),this.stateEl.classList.add(`c-slider__state`)}setParameters(){let{value:t,min:n,max:r,range:i,cssClass:a,tip:s,disabled:c,showValue:l,blockValueBelowCurrent:u,updateEvent:f,onUpdate:p}=this.options,[m,h]=i;this.el.classList.add(...a),this.setValue(t),this.setMin(n),this.setMax(r),this.setState(c),l&&this.setShowValue(t),this.setTip(s),this.setProgressBackground(),this.lastValue=t,thi
```
### 17
```js
`),this.stateEl=document.createElement(`div`),this.stateEl.classList.add(`c-slider__state`)}setParameters(){let{value:t,min:n,max:r,range:i,cssClass:a,tip:s,disabled:c,showValue:l,blockValueBelowCurrent:u,updateEvent:f,onUpdate:p}=this.options,[m,h]=i;this.el.classList.add(...a),this.setValue(t),this.setMin(n),this.setMax(r),this.setState(c),l&&this.setShowValue(t),this.setTip(s),this.setProgressBackground(),this.lastValue=t,this.input.addEventListener(`input`,n=>{let r=Number(t),i=Number(n.target.value);u&&i<r?(this.setValue(r),i=r):(i<m&&(this.setValue(m),i=m),i>h&&(this.setValue(h),i=h)),f===`input`&&p&&i!==this.lastValue&
```
### 18
```js
this.el=Templates_default.get(`checkbox-custom`)[0],this.inputEl=this.el.querySelector(`input`),this.labelEl=this.el.querySelector(`label`),this.createCheckbox(t)}createCheckbox({id:t,name:n,value:r,label:i,checked:a,attrs:s,i:c,highlight:l=!0,tip:u}){this.el.classList.add(`c-checkbox`),this.labelEl.classList.add(`c-checkbox__label`),l&&this.labelEl.classList.add(`c-checkbox__label--highlight`),this.inputEl.addEventListener(`change`,()=>{this.onSelected?.(this.getChecked())}),!isset$4(t)&&isset$4(c)&&(t=`${n}_${c}`),setAttributes(this.inputEl,{id:t,name:n,...r&&{value:r}}),a&&(this.inputEl.checked=!0),i?this.setLabel(i):this.
```
### 19
```js
ustom`)[0],this.inputEl=this.el.querySelector(`input`),this.labelEl=this.el.querySelector(`label`),this.createCheckbox(t)}createCheckbox({id:t,name:n,value:r,label:i,checked:a,attrs:s,i:c,highlight:l=!0,tip:u}){this.el.classList.add(`c-checkbox`),this.labelEl.classList.add(`c-checkbox__label`),l&&this.labelEl.classList.add(`c-checkbox__label--highlight`),this.inputEl.addEventListener(`change`,()=>{this.onSelected?.(this.getChecked())}),!isset$4(t)&&isset$4(c)&&(t=`${n}_${c}`),setAttributes(this.inputEl,{id:t,name:n,...r&&{value:r}}),a&&(this.inputEl.checked=!0),i?this.setLabel(i):this.el.classList.add(`checkbox-custom--alone`
```
### 20
```js
t`),this.labelEl=this.el.querySelector(`label`),this.createCheckbox(t)}createCheckbox({id:t,name:n,value:r,label:i,checked:a,attrs:s,i:c,highlight:l=!0,tip:u}){this.el.classList.add(`c-checkbox`),this.labelEl.classList.add(`c-checkbox__label`),l&&this.labelEl.classList.add(`c-checkbox__label--highlight`),this.inputEl.addEventListener(`change`,()=>{this.onSelected?.(this.getChecked())}),!isset$4(t)&&isset$4(c)&&(t=`${n}_${c}`),setAttributes(this.inputEl,{id:t,name:n,...r&&{value:r}}),a&&(this.inputEl.checked=!0),i?this.setLabel(i):this.el.classList.add(`checkbox-custom--alone`),u&&this.setTip(u),t&&this.labelEl.setAttribute(`f
```
### 21
```js
x__label--highlight`),this.inputEl.addEventListener(`change`,()=>{this.onSelected?.(this.getChecked())}),!isset$4(t)&&isset$4(c)&&(t=`${n}_${c}`),setAttributes(this.inputEl,{id:t,name:n,...r&&{value:r}}),a&&(this.inputEl.checked=!0),i?this.setLabel(i):this.el.classList.add(`checkbox-custom--alone`),u&&this.setTip(u),t&&this.labelEl.setAttribute(`for`,t.toString()),s&&setAttributes(this.el,s)}setTip(t){return $(this.el).tip(t)}setLabel(t){typeof t==`object`?this.labelEl.appendChild(t):this.labelEl.innerHTML=t}getCheckbox(){return this.el}getChecked(){return this.inputEl.checked}setChecked(t){this.inputEl.checked=t}toggleChecke
```
### 22
```js
){this.inputEl.value=t}},CheckboxList=class{constructor(t,n){this.checkboxes=[],this.container=n.container?n.container:document.createElement(`div`),this.returnType=n.returnType??`array`,this.onChange=n.onChange,this.createList(t)}createList(t){this.container.classList.add(`checkbox-list`),t.forEach((t,n)=>{t.i=n;let r=new Checkbox(t,()=>this.handleChange());this.checkboxes.push(r),this.container.appendChild(r.getCheckbox())})}handleChange(){this.onChange&&this.onChange(this.getSelected())}getComponent(){return this.container}getSelected(){if(this.returnType===`array`){let t=[];return this.checkboxes.forEach(n=>{n.getChecked(
```
### 23
```js
:a=this.createSlider(r);break;case FieldTypes$1.BUTTON:a=this.createButton(r);break;default:throwError(`FormBuilder.ts`,`createField`,`Field type "${r.type}" is not exist.`)}return r.createFullComponent&&(a=this.createFieldTemplate(a,r)),r.cssClass?.length&&a.classList.add(r.cssClass),r.wrapperElement?.appendChild(a),a}createFieldTemplate(t,n){let r=stringToHtml$1(this.fieldTemplate),i=r.querySelector(`.`+FormElementClass.LABEL);return n.label&&n.type!==FieldTypes$1.CHECKBOX?(i.textContent=n.label,n.labelTip&&$(i).tip(n.labelTip)):r.removeChild(i),r.querySelector(`.`+FormElementClass.CONTROL).appendChild(t),r}createInput(t){l
```
### 24
```js
Options});return t.control=n,n.getButton()}createLabel(t,n={}){let r=stringToHtml$1(this.fieldTemplate),i=r.querySelector(`.`+FormElementClass.CONTROL),a=r.querySelector(`.`+FormElementClass.LABEL);return a.textContent=t,r.removeChild(i),n.cssClass?.length&&r.classList.add(n.cssClass),n.wrapperElement?.appendChild(r),r}createSeparator(t={}){let n=document.createElement(`div`);return n.classList.add(FormElementClass.SEPARATOR_LINE),t.cssClass?.length&&n.classList.add(t.cssClass),t.wrapperElement?.appendChild(n),n}onChange(t,n){this.options.onChangeCallback?.(t,n)}changeValues(t){for(let n of this.fieldsData){let r=t[n.name];th
```
### 25
```js
rmElementClass.CONTROL),a=r.querySelector(`.`+FormElementClass.LABEL);return a.textContent=t,r.removeChild(i),n.cssClass?.length&&r.classList.add(n.cssClass),n.wrapperElement?.appendChild(r),r}createSeparator(t={}){let n=document.createElement(`div`);return n.classList.add(FormElementClass.SEPARATOR_LINE),t.cssClass?.length&&n.classList.add(t.cssClass),t.wrapperElement?.appendChild(n),n}onChange(t,n){this.options.onChangeCallback?.(t,n)}changeValues(t){for(let n of this.fieldsData){let r=t[n.name];this.changeSingleValue(n.name,r)}}changeSingleValue(t,n){let r=this.findFieldByName(t),i=r.control;switch(r.type){case FieldTypes$
```
### 26
```js
;return a.textContent=t,r.removeChild(i),n.cssClass?.length&&r.classList.add(n.cssClass),n.wrapperElement?.appendChild(r),r}createSeparator(t={}){let n=document.createElement(`div`);return n.classList.add(FormElementClass.SEPARATOR_LINE),t.cssClass?.length&&n.classList.add(t.cssClass),t.wrapperElement?.appendChild(n),n}onChange(t,n){this.options.onChangeCallback?.(t,n)}changeValues(t){for(let n of this.fieldsData){let r=t[n.name];this.changeSingleValue(n.name,r)}}changeSingleValue(t,n){let r=this.findFieldByName(t),i=r.control;switch(r.type){case FieldTypes$1.INPUT:i.val(String(n));break;case FieldTypes$1.MENU:i.setOptionWith
```
### 27
```js
Info(){let{id:t,nick:n,lvl:r,prof:i,account:a}=this.playerData,s=this.contentEl.querySelector(`.player-info`);s.appendChild(this.getLinkedPlayerName(n,t,a)),r!=0&&s.append(` (${r}${i})`)}getLinkedPlayerName(t,n,r){let i=document.createElement(`span`);return i.classList.add(`character-name`),i.textContent=t,i.addEventListener(`click`,n=>{n.stopPropagation(),Engine.chatController.getChatInputWrapper().setPrivateMessageProcedure(t)}),$(i).on(getRightClickEventName(),t=>{this.getEngine().others.createOtherContextMenu(t,{charId:this.playerData.id,accountId:this.playerData.account,...this.playerData},[OthersContextMenuData_default.
```
### 28
```js
,t=>{this.getEngine().others.createOtherContextMenu(t,{charId:this.playerData.id,accountId:this.playerData.account,...this.playerData},[OthersContextMenuData_default.SHOW_EQ])}),i}setAvatar(t){if(!t)return;let n=CFG.a_opath+t,r=document.createElement(`div`);r.classList.add(`avatar-icon`),createImgStyle($(r),n),this.contentEl.querySelector(`.prof-image`).appendChild(r)}initWindow(){this.contentEl=Templates_default.get(`show-eq`)[0];let t=Templates_default.get(`interface-element-equipment-with-additional-bag`)[0];t.classList.add(`other-items-wrapper`),this.contentEl.querySelector(`.other-items-wrapper`).replaceWith(t),this.getE
```
### 29
```js
.classList.add(`avatar-icon`),createImgStyle($(r),n),this.contentEl.querySelector(`.prof-image`).appendChild(r)}initWindow(){this.contentEl=Templates_default.get(`show-eq`)[0];let t=Templates_default.get(`interface-element-equipment-with-additional-bag`)[0];t.classList.add(`other-items-wrapper`),this.contentEl.querySelector(`.other-items-wrapper`).replaceWith(t),this.getEngine().windowManager.add({content:this.contentEl,nameWindow:this.getEngine().windowsData.name.SHOW_EQ,title:_t(`other_eq`),objParent:this,nameRefInParent:`wnd`,type:Engine.windowsData.type.TRANSPARENT,addClass:`showeq-window showeq-`+this.playerData.id,manag
```
### 30
```js
{},Tabs=class{constructor(t,n){this.cards=t,this.currentTab=null,this.tabElementList={},this.options={...defaultOptions$3,...n},this.createContent(),this.createCards()}createContent(){this.options.tabsEl.navEl&&(this.navEl=this.options.tabsEl.navEl,this.navEl.classList.add(`tabs-nav`)),this.options.tabsEl.contentsEl&&(this.contentsEl=this.options.tabsEl.contentsEl,this.contentsEl.classList.add(`tabs-contents`))}createCards(){for(let t in this.cards)this.createOneCard(t,this.cards[t])}createOneCard(t,n){let r,i,a;this.options.tabsEl.navEl?(r=Templates_default.getEl(`card`),a=r.querySelector(`.label`),r.classList.add(`${t}-tab`
```
### 31
```js
..n},this.createContent(),this.createCards()}createContent(){this.options.tabsEl.navEl&&(this.navEl=this.options.tabsEl.navEl,this.navEl.classList.add(`tabs-nav`)),this.options.tabsEl.contentsEl&&(this.contentsEl=this.options.tabsEl.contentsEl,this.contentsEl.classList.add(`tabs-contents`))}createCards(){for(let t in this.cards)this.createOneCard(t,this.cards[t])}createOneCard(t,n){let r,i,a;this.options.tabsEl.navEl?(r=Templates_default.getEl(`card`),a=r.querySelector(`.label`),r.classList.add(`${t}-tab`),a.innerHTML=n.name):r=n.tabEl,isset$4(n.disabled)&&n.disabled&&(r.classList.add(`disabled`),n.disabledTip&&$(r).tip(n.dis
```
### 32
```js
tabsEl.contentsEl,this.contentsEl.classList.add(`tabs-contents`))}createCards(){for(let t in this.cards)this.createOneCard(t,this.cards[t])}createOneCard(t,n){let r,i,a;this.options.tabsEl.navEl?(r=Templates_default.getEl(`card`),a=r.querySelector(`.label`),r.classList.add(`${t}-tab`),a.innerHTML=n.name):r=n.tabEl,isset$4(n.disabled)&&n.disabled&&(r.classList.add(`disabled`),n.disabledTip&&$(r).tip(n.disabledTip)),this.options.tabsEl.navEl&&this.navEl.appendChild(r),n.contentTargetEl?i=n.contentTargetEl:this.contentsEl&&(i=document.createElement(`div`),this.contentsEl.appendChild(i)),i?(this.addToTabElementList(t,r,i),i.class
```
### 33
```js
 this.cards)this.createOneCard(t,this.cards[t])}createOneCard(t,n){let r,i,a;this.options.tabsEl.navEl?(r=Templates_default.getEl(`card`),a=r.querySelector(`.label`),r.classList.add(`${t}-tab`),a.innerHTML=n.name):r=n.tabEl,isset$4(n.disabled)&&n.disabled&&(r.classList.add(`disabled`),n.disabledTip&&$(r).tip(n.disabledTip)),this.options.tabsEl.navEl&&this.navEl.appendChild(r),n.contentTargetEl?i=n.contentTargetEl:this.contentsEl&&(i=document.createElement(`div`),this.contentsEl.appendChild(i)),i?(this.addToTabElementList(t,r,i),i.classList.add(`${t}-content`),i.classList.add(`tabs-content-option`),n.contentToAppend&&i.appendC
```
### 34
```js
isabled`),n.disabledTip&&$(r).tip(n.disabledTip)),this.options.tabsEl.navEl&&this.navEl.appendChild(r),n.contentTargetEl?i=n.contentTargetEl:this.contentsEl&&(i=document.createElement(`div`),this.contentsEl.appendChild(i)),i?(this.addToTabElementList(t,r,i),i.classList.add(`${t}-content`),i.classList.add(`tabs-content-option`),n.contentToAppend&&i.appendChild(n.contentToAppend)):this.addToTabElementList(t,r),n.amount!==void 0&&this.updateAmount(t,n.amount.value);let s=getClickEventName$1();r.addEventListener(s,()=>{r.classList.contains(`disabled`)||(n.initAction?n.initAction():this.activateCard(t))})}updateAmount(t,n){let r=t
```
### 35
```js
p(n.disabledTip)),this.options.tabsEl.navEl&&this.navEl.appendChild(r),n.contentTargetEl?i=n.contentTargetEl:this.contentsEl&&(i=document.createElement(`div`),this.contentsEl.appendChild(i)),i?(this.addToTabElementList(t,r,i),i.classList.add(`${t}-content`),i.classList.add(`tabs-content-option`),n.contentToAppend&&i.appendChild(n.contentToAppend)):this.addToTabElementList(t,r),n.amount!==void 0&&this.updateAmount(t,n.amount.value);let s=getClickEventName$1();r.addEventListener(s,()=>{r.classList.contains(`disabled`)||(n.initAction?n.initAction():this.activateCard(t))})}updateAmount(t,n){let r=this.cards[t];if(!r||!r.amount)re
```
### 36
```js
.getCard(t).querySelector(`.amount`);i&&(n>0||(r.amount.showZero??!1)?(i.style.display=`block`,i.innerHTML=r.amount.template?r.amount.template.replace(`%value%`,n.toString()):n.toString()):i.style.display=`none`)}disableTab(t,n){let r=this.getCard(t);if(r&&(r.classList.add(`disabled`),this.cards[t].disabled=!0,n&&($(r).tip(n),this.cards[t].disabledTip=n),this.currentTab===t)){let t=this.getFirstAvailableCard();t&&this.activateCard(t)}}enableTab(t){let n=this.getCard(t);n&&(n.classList.remove(`disabled`),this.cards[t].disabled=!1,this.cards[t].disabledTip=void 0,$(n).tip(``))}setCurrentTab(t){this.currentTab=t}getCurrentTab(){
```
### 37
```js
Tab(t,n){let r=this.getCard(t);if(r&&(r.classList.add(`disabled`),this.cards[t].disabled=!0,n&&($(r).tip(n),this.cards[t].disabledTip=n),this.currentTab===t)){let t=this.getFirstAvailableCard();t&&this.activateCard(t)}}enableTab(t){let n=this.getCard(t);n&&(n.classList.remove(`disabled`),this.cards[t].disabled=!1,this.cards[t].disabledTip=void 0,$(n).tip(``))}setCurrentTab(t){this.currentTab=t}getCurrentTab(){return this.currentTab}callAfterShowFn(t){let n=this.cards[t];n.afterShowFn&&n.afterShowFn()}activateCard(t){this.currentTab!==t&&(this.setCurrentTab(t),this.addActiveForCurrentTab(t),this.removeActiveForOtherTabs(t),this.c
```
### 38
```js
s[t];n.afterShowFn&&n.afterShowFn()}activateCard(t){this.currentTab!==t&&(this.setCurrentTab(t),this.addActiveForCurrentTab(t),this.removeActiveForOtherTabs(t),this.callAfterShowFn(t))}addActiveForCurrentTab(t){let n=this.getCard(t),r=this.getCardContent(t);n.classList.add(`active`),r?.classList.add(`active`)}removeActiveForOtherTabs(t){Object.keys(this.tabElementList).filter(n=>n!==t).forEach(t=>{let n=this.tabElementList[t];n.tab.classList.remove(`active`),n.content?.classList.remove(`active`)})}addToTabElementList(t,n,r){r===void 0?this.tabElementList[t]={tab:n}:this.tabElementList[t]={tab:n,content:r}}getCard(t){return th
```
### 39
```js
ShowFn()}activateCard(t){this.currentTab!==t&&(this.setCurrentTab(t),this.addActiveForCurrentTab(t),this.removeActiveForOtherTabs(t),this.callAfterShowFn(t))}addActiveForCurrentTab(t){let n=this.getCard(t),r=this.getCardContent(t);n.classList.add(`active`),r?.classList.add(`active`)}removeActiveForOtherTabs(t){Object.keys(this.tabElementList).filter(n=>n!==t).forEach(t=>{let n=this.tabElementList[t];n.tab.classList.remove(`active`),n.content?.classList.remove(`active`)})}addToTabElementList(t,n,r){r===void 0?this.tabElementList[t]={tab:n}:this.tabElementList[t]={tab:n,content:r}}getCard(t){return this.tabElementList[t].tab}ge
```
### 40
```js
owFn(t))}addActiveForCurrentTab(t){let n=this.getCard(t),r=this.getCardContent(t);n.classList.add(`active`),r?.classList.add(`active`)}removeActiveForOtherTabs(t){Object.keys(this.tabElementList).filter(n=>n!==t).forEach(t=>{let n=this.tabElementList[t];n.tab.classList.remove(`active`),n.content?.classList.remove(`active`)})}addToTabElementList(t,n,r){r===void 0?this.tabElementList[t]={tab:n}:this.tabElementList[t]={tab:n,content:r}}getCard(t){return this.tabElementList[t].tab}getCardContent(t){return this.tabElementList[t].content}checkRequires(){for(let t in this.cards){let n=this.cards[t];if(isset$4(n.disabled)&&n.disabled)co
```
_Only first 40 of 223 matches shown._

## transform
Matches: **37**

### 1
```js
}},this.getCssPosition=t=>{let n=Engine.interface.checkEqColumnIsShow(),r=Engine.interface.centerObjectCoverEqColumn(t),i=this.$.hasClass(`is-open`)?0:100,a=getEngine().ResolutionData.KEY._DEFAULT,s=getEngine().resolution.getResolutionKey();return n&&s==a&&r?{transform:`translate(0%, `+i+`%)`,left:Engine.interface.getXPosOfObjectStickToEqColumn(t)}:{transform:`translate(-50%, `+i+`%)`,left:`50%`}},this.endTalk=function(){this.finish(),v.id=0,Engine.lock.remove(`npcdialog`),delete v.block},this.finish=function(){this.setTutorial(v.id,2),r&&(this.$.removeClass(`is-open`),this.setSizeAndPosOfNormalDialog()),n=!1,Engine.items
```
### 2
```js
enterObjectCoverEqColumn(t),i=this.$.hasClass(`is-open`)?0:100,a=getEngine().ResolutionData.KEY._DEFAULT,s=getEngine().resolution.getResolutionKey();return n&&s==a&&r?{transform:`translate(0%, `+i+`%)`,left:Engine.interface.getXPosOfObjectStickToEqColumn(t)}:{transform:`translate(-50%, `+i+`%)`,left:`50%`}},this.endTalk=function(){this.finish(),v.id=0,Engine.lock.remove(`npcdialog`),delete v.block},this.finish=function(){this.setTutorial(v.id,2),r&&(this.$.removeClass(`is-open`),this.setSizeAndPosOfNormalDialog()),n=!1,Engine.items.removeCallback(Engine.itemsFetchData.NEW_QUEST_REWARD_ITEM),t.itemsClear(),v.npc={},Engine.
```
### 3
```js
rtClassBrand(_Swiper_brand,this,_clampIndex).call(this,t);_classPrivateFieldSet2(_index$1,this,i);let a=_assertClassBrand(_Swiper_brand,this,_effectiveSlideSize).call(this),s=-i*a;_classPrivateFieldSet2(_left,this,s),_assertClassBrand(_Swiper_brand,this,_applyTransform).call(this,s,r),_assertClassBrand(_Swiper_brand,this,_updatePagination).call(this),_classPrivateFieldGet2(_opts,this).onChange(i,this)}};function _isInfiniteSlide(){return _classPrivateFieldGet2(_opts,this).infinite&&_classPrivateFieldGet2(_opts,this).mode===`slide`}function _goToTrackIndex(t,n=!0){let r=_classPrivateFieldGet2(_baseSlidesCount,this),i=_clas
```
### 4
```js
t=_assertClassBrand(_Swiper_brand,this,_wrapIntoRealZone).call(this,t,a)),_classPrivateFieldSet2(_trackIndex,this,t),_classPrivateFieldSet2(_index$1,this,((t-i)%r+r)%r);let s=-t*a;_classPrivateFieldSet2(_left,this,s),_assertClassBrand(_Swiper_brand,this,_applyTransform).call(this,s,n),_assertClassBrand(_Swiper_brand,this,_updatePagination).call(this),_classPrivateFieldGet2(_opts,this).onChange(_classPrivateFieldGet2(_index$1,this),this)}function _wrapIntoRealZone(t,n){let r=_classPrivateFieldGet2(_baseSlidesCount,this),i=_classPrivateFieldGet2(_cloneCount,this);if(t>=i&&t<i+r)return t;let a=((t-i)%r+r)%r+i,s=a-t,c=_assert
```
### 5
```js
classPrivateFieldGet2(_baseSlidesCount,this),i=_classPrivateFieldGet2(_cloneCount,this);if(t>=i&&t<i+r)return t;let a=((t-i)%r+r)%r+i,s=a-t,c=_assertClassBrand(_Swiper_brand,this,_currentTranslateX).call(this);return _assertClassBrand(_Swiper_brand,this,_applyTransform).call(this,c-s*n,!1),_classPrivateFieldGet2(_track,this).offsetWidth,a}function _currentTranslateX(){let t=getComputedStyle(_classPrivateFieldGet2(_track,this)).transform;if(!t||t===`none`)return _classPrivateFieldGet2(_left,this);let n=t.match(/matrix(3d)?\(([^)]+)\)/);if(!n)return _classPrivateFieldGet2(_left,this);let r=n[2].split(`,`).map(t=>parseFloat(
```
### 6
```js
nd,this,_currentTranslateX).call(this);return _assertClassBrand(_Swiper_brand,this,_applyTransform).call(this,c-s*n,!1),_classPrivateFieldGet2(_track,this).offsetWidth,a}function _currentTranslateX(){let t=getComputedStyle(_classPrivateFieldGet2(_track,this)).transform;if(!t||t===`none`)return _classPrivateFieldGet2(_left,this);let n=t.match(/matrix(3d)?\(([^)]+)\)/);if(!n)return _classPrivateFieldGet2(_left,this);let r=n[2].split(`,`).map(t=>parseFloat(t)),i=n[1]?r[12]:r[4];return Number.isFinite(i)?i:_classPrivateFieldGet2(_left,this)}function _bindTransitionEnd(){_assertClassBrand(_Swiper_brand,this,_isInfiniteSlide).c
```
### 7
```js
:r[4];return Number.isFinite(i)?i:_classPrivateFieldGet2(_left,this)}function _bindTransitionEnd(){_assertClassBrand(_Swiper_brand,this,_isInfiniteSlide).call(this)&&_classPrivateFieldGet2(_track,this).addEventListener(`transitionend`,t=>{if(t.propertyName!==`transform`)return;let n=_classPrivateFieldGet2(_baseSlidesCount,this),r=_classPrivateFieldGet2(_cloneCount,this);(_classPrivateFieldGet2(_trackIndex,this)<r||_classPrivateFieldGet2(_trackIndex,this)>=r+n)&&_assertClassBrand(_Swiper_brand,this,_goToTrackIndex).call(this,r+_classPrivateFieldGet2(_index$1,this),!1)})}function _setupStructure(){_classPrivateFieldGet2(_ro
```
### 8
```js
his).onDrag(this),t.preventDefault()),_classPrivateFieldSet2(_lastX,this,n),_classPrivateFieldSet2(_lastTime,this,performance.now());let i=_classPrivateFieldGet2(_startLeft,this)+r;_classPrivateFieldSet2(_left,this,i),_classPrivateFieldGet2(_track,this).style.transform=`translate3d(${i}px, 0, 0)`}),_classPrivateFieldGet2(_track,this).addEventListener(`pointerup`,t=>{if(!_classPrivateFieldGet2(_isDragging,this))return;_classPrivateFieldSet2(_isDragging,this,!1),_classPrivateFieldGet2(_dragStarted,this)&&_classPrivateFieldGet2(_track,this).hasPointerCapture(t.pointerId)&&_classPrivateFieldGet2(_track,this).releasePointerCap
```
### 9
```js
(_index$1,this)-a,c=_assertClassBrand(_Swiper_brand,this,_maxIndex).call(this),l=_classPrivateFieldGet2(_opts,this).loop?(s%(c+1)+(c+1))%(c+1):Math.min(c,Math.max(0,s));this.goTo(l)}function _computeSteps(t,n){return Math.max(1,Math.round(t/n))}function _applyTransform(t,n){_classPrivateFieldGet2(_track,this).style.transition=n?`transform 0.25s ease-out`:`none`,_classPrivateFieldGet2(_track,this).style.transform=`translate3d(${t}px, 0, 0)`}function _effectiveSlideSize(){return _classPrivateFieldGet2(_opts,this).slideSize?_classPrivateFieldGet2(_opts,this).slideSize:_classPrivateFieldGet2(_slides,this)[0]?.offsetWidth||0}f
```
### 10
```js
l(this),l=_classPrivateFieldGet2(_opts,this).loop?(s%(c+1)+(c+1))%(c+1):Math.min(c,Math.max(0,s));this.goTo(l)}function _computeSteps(t,n){return Math.max(1,Math.round(t/n))}function _applyTransform(t,n){_classPrivateFieldGet2(_track,this).style.transition=n?`transform 0.25s ease-out`:`none`,_classPrivateFieldGet2(_track,this).style.transform=`translate3d(${t}px, 0, 0)`}function _effectiveSlideSize(){return _classPrivateFieldGet2(_opts,this).slideSize?_classPrivateFieldGet2(_opts,this).slideSize:_classPrivateFieldGet2(_slides,this)[0]?.offsetWidth||0}function _pageCount(){if(_assertClassBrand(_Swiper_brand,this,_isInfinit
```
### 11
```js
h.min(c,Math.max(0,s));this.goTo(l)}function _computeSteps(t,n){return Math.max(1,Math.round(t/n))}function _applyTransform(t,n){_classPrivateFieldGet2(_track,this).style.transition=n?`transform 0.25s ease-out`:`none`,_classPrivateFieldGet2(_track,this).style.transform=`translate3d(${t}px, 0, 0)`}function _effectiveSlideSize(){return _classPrivateFieldGet2(_opts,this).slideSize?_classPrivateFieldGet2(_opts,this).slideSize:_classPrivateFieldGet2(_slides,this)[0]?.offsetWidth||0}function _pageCount(){if(_assertClassBrand(_Swiper_brand,this,_isInfiniteSlide).call(this))return _classPrivateFieldGet2(_baseSlidesCount,this);if(
```
### 12
```js
a=i[this.getValueOfBanner(t-1)],s=r[a],l=this.createBanner(a,s.btn,s.clb);n.find(`.all-b`).prepend(l);let u=n.find(`.all-b`),f=()=>{u.children().last().remove(),c=!1};if(isSettingsOptionsInterfaceAnimationOn()){let t=document.querySelector(`.all-b`).animate([{transform:`translateX(-476px)`},{transform:`translateX(-238px)`}],{duration:500,easing:`cubic-bezier(0.33, 1, 0.68, 1)`,fill:`forwards`});t.onfinish=f}else f()},this.rightBtnClick=()=>{if(c)return;c=!0;let a=i.length-1;t<a?t++:t=0;let s=i[this.getValueOfBanner(t+1)],l=r[s],u=this.createBanner(s,l.btn,l.clb);this.addBannerToWrapper(u);let f=n.find(`.all-b`),p=()=>{f.c
```
### 13
```js
=r[a],l=this.createBanner(a,s.btn,s.clb);n.find(`.all-b`).prepend(l);let u=n.find(`.all-b`),f=()=>{u.children().last().remove(),c=!1};if(isSettingsOptionsInterfaceAnimationOn()){let t=document.querySelector(`.all-b`).animate([{transform:`translateX(-476px)`},{transform:`translateX(-238px)`}],{duration:500,easing:`cubic-bezier(0.33, 1, 0.68, 1)`,fill:`forwards`});t.onfinish=f}else f()},this.rightBtnClick=()=>{if(c)return;c=!0;let a=i.length-1;t<a?t++:t=0;let s=i[this.getValueOfBanner(t+1)],l=r[s],u=this.createBanner(s,l.btn,l.clb);this.addBannerToWrapper(u);let f=n.find(`.all-b`),p=()=>{f.children().first().remove(),c=!1};
```
### 14
```js
s=i[this.getValueOfBanner(t+1)],l=r[s],u=this.createBanner(s,l.btn,l.clb);this.addBannerToWrapper(u);let f=n.find(`.all-b`),p=()=>{f.children().first().remove(),c=!1};if(isSettingsOptionsInterfaceAnimationOn()){let t=document.querySelector(`.all-b`).animate([{transform:`translateX(-238px)`},{transform:`translateX(-476px)`}],{duration:500,easing:`cubic-bezier(0.33, 1, 0.68, 1)`,fill:`backwards`});t.onfinish=p}else p();this.startInterval()},this.getNow=()=>t,this.onResize=()=>{this.update()},this.initDataBanners=()=>{r=isPl()?BannersDataPl:BannersDataEn}}function Help2(){var t,n=this,r=null;this.$profsanditems=null,this.$en
```
### 15
```js
=r[s],u=this.createBanner(s,l.btn,l.clb);this.addBannerToWrapper(u);let f=n.find(`.all-b`),p=()=>{f.children().first().remove(),c=!1};if(isSettingsOptionsInterfaceAnimationOn()){let t=document.querySelector(`.all-b`).animate([{transform:`translateX(-238px)`},{transform:`translateX(-476px)`}],{duration:500,easing:`cubic-bezier(0.33, 1, 0.68, 1)`,fill:`backwards`});t.onfinish=p}else p();this.startInterval()},this.getNow=()=>t,this.onResize=()=>{this.update()},this.initDataBanners=()=>{r=isPl()?BannersDataPl:BannersDataEn}}function Help2(){var t,n=this,r=null;this.$profsanditems=null,this.$environment=null,this.$premium=null
```
### 16
```js
elector(this.selector),!this.el)throw Error(`DragZoom: not found element with selector "${this.selector}"`);if(this.zoomedEl=this.el.firstElementChild,!this.zoomedEl)throw Error(`DragZoom: not found child element for zooming and dragging`);this.zoomedEl.style.transformOrigin=`0 0`,this.el.style.touchAction=`none`}setOptions(){this.options={...this.defaultOptions,...this.passedOptions},this.options.factor/=100}connectEvents(){this.el.addEventListener(`wheel`,this.onWheel),this.el.addEventListener(`pointerdown`,this.onPointerDown)}addGlobalListeners(){document.addEventListener(`pointermove`,this.onPointerMove),document.addE
```
### 17
```js
e(1),t&&this.setMatrix()}resetScaleAndPosition(){this.resetScale(!1),this.resetPosition(!1),this.setMatrix()}setMatrix(){let t=`matrix(${this.scale}, 0, 0, ${this.scale}, ${this.pos.x}, ${this.pos.y})`;return typeof RUNNING_UNIT_TEST>`u`&&(this.zoomedEl.style.transform=t),t}getOuterZoom(){return this.roundToTwo(this.el.getBoundingClientRect().width/this.el.offsetWidth)}roundToTwo(t){return+(Math.round(t+`e+2`)+`e-2`)}};function MiniMapController(){var t=this;this.$=null,this.handHeldMiniMapController=null;var n=null,r=null,i=!1,a=!1,s=null,c,l;let u,f=null;this.getMiniMapShow=function(){return i},this.init=function(){this
```
### 18
```js
let n in t){let r=t[n],i=r.id,a=r.link;if(i!=v)continue;let s=null;s=a==``?`none`:`url("${r.link}") no-repeat center center`,k.css(`background`,s);return}errorReport(r.fileName,`updateBackgroundUrl`,`id not find!`,v),k.css(`background`,`none`)},ee=()=>{k.css(`transform`,`scale(${y})`)},te=()=>{k.css(`opacity`,ne(b))},ne=t=>t/10,re=()=>{O=Ke(),se(),G(),I(),L(),R(),z(),ie()},ie=()=>{F=O.find(`.scale-input-wrapper`).empty();let t=createNiInput({cl:`asdasd`,type:InputMaskData_default.TYPE.NUMBER_FLOAT,tipClearClb:_t(`reset`,null,`ah_filter_history`),keyUpClb:(t,n)=>{ae(t,n)},focusoutClb:()=>{oe(F.find(`input`).val())},clearCl
```
### 19
```js
on-opt {         color: white;       }        #${t} .one-opt-record .input-opt  {         width: 60%;       }        .main-checkBox-wrapper {         margin-bottom: 10px;       }        			.window-mode-background-layer {         pointer-events:none;         //transform: scale(1.5); 			}        body[data-res="${n._920_X_555}"],       body[data-res="${n._1173_X_555}"], 			body[data-res="${n._1024_X_768}"], 			body[data-res="${n._1277_X_768}"], 			body[data-res="${n._1366_X_768}"], 			body[data-res="${n._1619_X_768}"], 			body[data-res="${n._1200_X_675}"], 			body[data-res="${n._1253_X_675}"], 			body[data-res="${n._1600_X_9
```
### 20
```js
              }                 }  	        }              body[data-res="${n._920_X_555}"] { 			    .pre-captcha { 			        top:-22px; 			    } 			    .pre-captcha.show { 			        top:52px; 			    } 			    .interface-layer .battle-controller { 			        transform: scale(0.75);                     -webkit-transform-origin-y: 100%; 			    }             }              body[data-res="${n._920_X_555}"] {                 /*                 .bottom-left.main-buttons-container {                     bottom: -11px;                 }                 .bottom-right.main-buttons-container {                     bottom: -11px;     
```
### 21
```js
       body[data-res="${n._920_X_555}"] { 			    .pre-captcha { 			        top:-22px; 			    } 			    .pre-captcha.show { 			        top:52px; 			    } 			    .interface-layer .battle-controller { 			        transform: scale(0.75);                     -webkit-transform-origin-y: 100%; 			    }             }              body[data-res="${n._920_X_555}"] {                 /*                 .bottom-left.main-buttons-container {                     bottom: -11px;                 }                 .bottom-right.main-buttons-container {                     bottom: -11px;                 }                 */                 .ma
```
### 22
```js
    .bottom-right.main-buttons-container {                     bottom: -11px;                 }                 */                 .main-buttons-container {                     width: 226px                 }                 .trade-window {                     transform: scale(0.72);                     bottom: 16px;                 }             }              body[data-res="${n._1024_X_768}"] {                  .pre-captcha { 			        top:-18px; 			    } 			    .pre-captcha.show { 			        top:52px; 			    }                 .trade-window {                     transform: scale(0.9);                     bottom: 42px;  
```
### 23
```js
 16px;                 }             }              body[data-res="${n._1024_X_768}"] {                  .pre-captcha { 			        top:-18px; 			    } 			    .pre-captcha.show { 			        top:52px; 			    }                 .trade-window {                     transform: scale(0.9);                     bottom: 42px;                 }             }              body[data-res="${n._1173_X_555}"] {                 .pre-captcha { 			        top:-20px; 			    } 			    .pre-captcha.show { 			        top:55px; 			    }                 .trade-window {                     bottom: 42px;                 }             }              b
```
### 24
```js
battle-controller.with-skills { 			        bottom: 50px; 			    } 			    .interface-layer .mini-map-controller { 			        top:50px; 			        bottom: 50px; 			    }  			    .hud-container, 			    .bottom-panel-of-bottom-positioner.bottom-panel { 			        transform: scale(0.82); 			    } 			    .hud-container { 	                -webkit-transform-origin-y: 10%;                 }                 .bottom-panel-of-bottom-positioner.bottom-panel { 	                transform-origin: 50% 100%;                 }                 .interface-layer .top.positioner .bg {                     background-position-y: -71px!important; 
```
### 25
```js
e-layer .mini-map-controller { 			        top:50px; 			        bottom: 50px; 			    }  			    .hud-container, 			    .bottom-panel-of-bottom-positioner.bottom-panel { 			        transform: scale(0.82); 			    } 			    .hud-container { 	                -webkit-transform-origin-y: 10%;                 }                 .bottom-panel-of-bottom-positioner.bottom-panel { 	                transform-origin: 50% 100%;                 }                 .interface-layer .top.positioner .bg {                     background-position-y: -71px!important;                 }                 .bottom-left.main-buttons-container {           
```
### 26
```js
anel-of-bottom-positioner.bottom-panel { 			        transform: scale(0.82); 			    } 			    .hud-container { 	                -webkit-transform-origin-y: 10%;                 }                 .bottom-panel-of-bottom-positioner.bottom-panel { 	                transform-origin: 50% 100%;                 }                 .interface-layer .top.positioner .bg {                     background-position-y: -71px!important;                 }                 .bottom-left.main-buttons-container {                     left: 2px;                 }                 .bottom-right.main-buttons-container {                     right: 2px; 
```
### 27
```js
dget-left,                 .layer.interface-layer .positioner.bottom .bg-additional-widget-right {                     bottom: -20px;                 }                  .layer.interface-layer .positioner.bottom .bg-additional-widget-left {                     transform: scale(-1, 0.82);                     transform-origin: 50% -5%;                 }                 .layer.interface-layer .positioner.bottom .bg-additional-widget-right {                     transform: scale(1, 0.82);                     transform-origin: 0% -5%;                 }              }              body[data-res="${n._1024_X_768}"],             bo
```
### 28
```js
r .positioner.bottom .bg-additional-widget-right {                     bottom: -20px;                 }                  .layer.interface-layer .positioner.bottom .bg-additional-widget-left {                     transform: scale(-1, 0.82);                     transform-origin: 50% -5%;                 }                 .layer.interface-layer .positioner.bottom .bg-additional-widget-right {                     transform: scale(1, 0.82);                     transform-origin: 0% -5%;                 }              }              body[data-res="${n._1024_X_768}"],             body[data-res="${n._1173_X_555}"] { 			    .hud-co
```
### 29
```js
er.bottom .bg-additional-widget-left {                     transform: scale(-1, 0.82);                     transform-origin: 50% -5%;                 }                 .layer.interface-layer .positioner.bottom .bg-additional-widget-right {                     transform: scale(1, 0.82);                     transform-origin: 0% -5%;                 }              }              body[data-res="${n._1024_X_768}"],             body[data-res="${n._1173_X_555}"] { 			    .hud-container, 			    .bottom-panel-of-bottom-positioner.bottom-panel { 			        transform: scale(0.9); 			    } 			}  		</style> 	`}}var addonsScripts={addo
```
### 30
```js
            transform: scale(-1, 0.82);                     transform-origin: 50% -5%;                 }                 .layer.interface-layer .positioner.bottom .bg-additional-widget-right {                     transform: scale(1, 0.82);                     transform-origin: 0% -5%;                 }              }              body[data-res="${n._1024_X_768}"],             body[data-res="${n._1173_X_555}"] { 			    .hud-container, 			    .bottom-panel-of-bottom-positioner.bottom-panel { 			        transform: scale(0.9); 			    } 			}  		</style> 	`}}var addonsScripts={addon_1:_1,addon_3:_3,addon_7:_7,addon_8:_8,addon_1
```
### 31
```js
              transform-origin: 0% -5%;                 }              }              body[data-res="${n._1024_X_768}"],             body[data-res="${n._1173_X_555}"] { 			    .hud-container, 			    .bottom-panel-of-bottom-positioner.bottom-panel { 			        transform: scale(0.9); 			    } 			}  		</style> 	`}}var addonsScripts={addon_1:_1,addon_3:_3,addon_7:_7,addon_8:_8,addon_11:_11,addon_19:_19,addon_21:_21,addon_24:_24,addon_25:_25,addon_27:_27,addon_28:_28};addonsScripts.addon_17&&(errorReport$1(`AddonsPanel.js`,`AddonsPanel.js`,`In past addon_17 was minutnik addon. Now minutnik has embeded in interface and use addo
```
### 32
```js
:1,r=Engine.battle.getBattleArea(),i=this.getAvailableHeightForBattleArea(),a=this.getAvailableWidthForBattleArea(),s=this.getMaxBattleGroundHeight(),c=a/this.getMaxSumWidthOfLine();c=c>1?1:c;let l=i/s;l=l>1?1:l,t=c<1||l<1?Math.min(c,l):1;let u=i*1/n/2;r.css(`transform`,`translate(-50%, -50%) scale(`+t+`)`),r.css(`top`,u+`px`)},this.getFirstTakenLine=()=>{let t=Engine.battle.warriors.getLines();for(let n=0;n<t.length;n++)if(t[n].length)return n;return null},this.getLastTakenLine=()=>{let t=Engine.battle.warriors.getLines();for(let n=t.length-1;n>-1;n--)if(t[n].length)return n;return null},this.getMaxHeightMob=()=>{let t=E
```
### 33
```js
splay`,`none`),r=!1,c++,Engine.battle.battleEffectsController.afterStopAction(this,c,i)},this.getTint=()=>r?[]:[self]}function BattleEarthQuakeAction(){let t,n,r,i=1;this.init=()=>{},this.updateData=t=>{r=t},this.start=()=>{t&&this.stop(),Engine.battle.$.css({transform:`scale(1.05)`}),t=setInterval(()=>{let t=Math.sin(Math.random())*15,n=Math.sin(Math.random())*15;Engine.battle.$.css({top:t,left:n})},50),n=setTimeout(()=>{Engine.battle.$.css({transform:`scale(1.0)`,left:0,top:0}),this.stop()},r.data.params.duration*1e3)},this.stop=()=>{clearInterval(t),clearTimeout(n),i++,Engine.battle.battleEffectsController.afterStopAct
```
### 34
```js
.updateData=t=>{r=t},this.start=()=>{t&&this.stop(),Engine.battle.$.css({transform:`scale(1.05)`}),t=setInterval(()=>{let t=Math.sin(Math.random())*15,n=Math.sin(Math.random())*15;Engine.battle.$.css({top:t,left:n})},50),n=setTimeout(()=>{Engine.battle.$.css({transform:`scale(1.0)`,left:0,top:0}),this.stop()},r.data.params.duration*1e3)},this.stop=()=>{clearInterval(t),clearTimeout(n),i++,Engine.battle.battleEffectsController.afterStopAction(this,i,r)}}function TintWarriorAction(){let t,n,r=3.14,i=!1,a,s=1,c=0,l=null;this.init=()=>{},this.updateData=(n,r)=>{t=n,l=r},this.start=()=>{n=0,i=!0},this.stop=()=>{i=!1,s++,Engine
```
### 35
```js
riorID=null,this.showedSkills=null,this.heroMana=null,this.heroEnergy=null,this.show=!1,pe(!0)},this.init=function(){this.initVariable(),this.initBattleWindow(),this.initBattleController(),this.initObjects(),this.setPredictionScrollbar(),this.zoomMode||y.css(`transform`,`translateX(-50%)`),V=new BattlePredictionHelpWindow,V.init(),H=new BattleHotSkillsHelpWindow,H.init(),B=m[0].querySelector(`.turn-prediction`)},this.getFlist1=()=>w,this.getFlist2=()=>T,this.getTeamIDs=()=>r,this.initProgressBars=function(){var t=m.find(`.stats-wrapper`);this.createProgressBar(t,`hp-progress-bar red`),this.createProgressBar(t,`ep-progress
```
### 36
```js
tleNight.rebuildBattleNight(t)};this.setWatchPosition=function(){},this.updateBattleground=function(n){let r=t.$.find(`.battle-background`);var i=ce[n]?ce[n]:n.replace(/si/g,`ni`),a=CFG.a_bpath+i;i==`matchmaking.jpg`&&(a=`img/bg-match/matchmaking.jpg`),r.css(`transform`,`translate(-50%,-50%) scale(2.0)`),Engine.imgLoader.onload(a,null,null,n=>{r.css(`background`,`url(`+n.src+`)`),t.onResize()})},this.joinStrFromObjects=(t,n,r)=>{let i=[];for(let r in t)i.push(t[r][n]);return i.join(r)};let fe=t=>{for(let n in t)this.warriorsList[n].updateDrawOrNoSkillsAnimation()};this.updateWarriors=function(n){if(!r[1].length){for(var i
```
### 37
```js
icLayer(o$19.$_M_ALERT_LAYER),Engine.windowManager.updatePosOfWindowsInSpecificLayer(o$19.$_CONSOLE_LAYER)},this.resizeScreen=function(){let t=Engine.zoomFactor?Engine.zoomFactor:1,n=$(`body`);n.width(window.innerWidth/t),n.height(window.innerHeight/t),n.css(`transform`,`scale(`+t+`)`)},this.setCTXScaleMode=function(t){t===1?this.mode=function(t,n){var r=1;isset(window.devicePixelRatio)&&(r=Math.round(window.devicePixelRatio*100)/100);var i=Math.round(t*r),a=Math.round(n*r);i+=i%2,a+=a%2;var s=Math.round(i/r),c=Math.round(a/r);return{canvas:{width:i,height:a},css:{width:s,height:c},store:{width:s,height:c},scale:r}}:t===2
```

## Relevant string literals
Unique matches: **175**

- `header-label-positioner`
- `positioner`
- `chat-layer layer`
- `chat-overlay`
- `chat-modal`
- `chat-header-mobile`
- `left-column main-column`
- `right-column main-column`
- `extended-stats scroll-wrapper small-bar`
- `top positioner`
- `data-tip#iconchat`
- `top-left-column-visibility-toggle column-visibility-toggle`
- `top-right-column-visibility-toggle column-visibility-toggle`
- `hud-container`
- `under-top positioner`
- `bottom positioner`
- `bottom-panel-of-bottom-positioner bottom-panel`
- `bottom-panel-graphic`
- `bottom-panel-pointer-bg`
- `mini-map-controller mini-map`
- `mini-map-header`
- `mini-map-label`
- `mini-map-map`
- `mini-map-mouse-move`
- `mini-map-panel`
- `mini-map-buttons`
- `mini-map-content`
- `extended-stats-tpl scroll-pane`
- `stats-section`
- `stats_attack`
- `stat-row damage-normal warrior-stats`
- `stat-row damage-offhand warrior-stats`
- `stat-row damage-fire warrior-stats`
- `stat-row damage-lightning warrior-stats`
- `stat-row damage-cold warrior-stats`
- `stat-row damage-poison warrior-stats`
- `stat-row damage-poison1 warrior-stats`
- `stat-row damage-of_poison1 warrior-stats`
- `stat-row damage-poison0 warrior-stats`
- `stat-row damage-wound0 warrior-stats`
- `stat-row damage-wound1 warrior-stats`
- `stat-row damage-of_wound0 warrior-stats`
- `stat-row damage-of_wound1 warrior-stats`
- `stat-row warrior-stats`
- `stats_defence`
- `stat-row warrior-stats text-stat`
- `stats_power`
- `stats_basic`
- `stats_aux`
- `passive-stats-header`
- `stat-row passive-stats`
- `stats-section legends`
- `interface-element-equipment-with-additional-bag`
- `equipment-wrapper-outline`
- `equipment-outline-1 equipment-outline`
- `equipment-outline-2 equipment-outline`
- `equipment-outline-3 equipment-outline`
- `equipment-outline-4 equipment-outline`
- `interface-element-equipment`
- `stats-light-mode interface-element-grid-border`
- `stats-light-mode interface-element-grid-border-light`
- `stats-border interface-element-background-color-3 interface-element-box-shadow-2`
- `stats-button`
- `stats-list-line`
- `stats-list`
- `data-tip#attack#stats`
- `data-tip#attack-speed#stats`
- `data-tip#defence#stats`
- `data-tip#resists#stats`
- `resist-stats`
- `equipment-wrapper`
- `stats-wrapper interface-element-background-color-3 interface-element-box-shadow-2 interface-element-grid-border`
- `#stats-head-title#stats`
- `inventory_wrapper`
- `inventory-grid-bg interface-element-grid-border`
- `inventory-grid`
- `right-column-notif`
- `console-bottom-panel-wrapper`
- `console-bottom-panel`
- `bottom-panel-graphics`
- `mini-map-local-content`
- `border-wrapper-mini-map`
- `element-mini-map element`
- `mini-map-global-content`
- `handheld-mini-map`
- `handheld-mini-map-canvas`
- `icons-column-mini-map icons-column mm-mark-list`
- `first-column-mini-map first-column`
- `second-column-mini-map second-column`
- `color-to-choose-mini-map color-to-choose`
- `mini-map-other other mark`
- `mini-map-gateway gateway mark`
- `mini-map-rip rip mark`
- `mini-map-monster monster mark`
- `mini-map-recovery recovery mark`
- `chat-message`
- `color-chat-msg`
- `chat-tab tab`
- `t_chat_card`
- `chat-ban`
- `shop-right-column`
- `left-column`
- `stats-wrapper`
- `right-column`
- `stats`
- `char-stats`
- `package-positioner`
- `tile-items-positioner`
- `top-left-column-graphics`
- `middle-left-column-graphics`
- `bottom-left-column-graphics`
- `left-column-header`
- `right-column-header`
- `left-column-auction-and-main-column-auction interface-element-vertical-wood`
- `left-column-auction`
- `scroll-wrapper left-column-scroll classic-bar`
- `stats-wrapper stone interface-element-active-card-border-image`
- `stats-h`
- `#stats_header#skills`
- `all-stats`
- `opt_${RECEIVE_PRIVATE_CHAT_MESSAGE}`
- `opt_${CLAN_MEMBER_ENTRY_CHAT_MESSAGE}`
- `opt_${FRIEND_ENTRY_CHAT_MESSAGE}`
- `opt_${ADD_OR_REMOVE_PARTY_MEMBER_CHAT_MESSAGE}`
- `show-hand-held-mini-map-checkbox-wrapper`
- `matchmaking-menu-bottom-panel`
- `choose-eq-bottom-panel`
- `stats-and-history main-wnd`
- `stats-and-history-tabs`
- `progress-bottom-panel`
- `stats-wnd section`
- `stats-table`
- `stats-bottom-panel`
- `stats-info`
- `history-bottom-panel`
- `season-bottom-panel`
- `statistics-detailed-bottom-panel`
- `ladder_global-bottom-panel ranking-bottom-panel`
- `ladder_clan-bottom-panel ranking-bottom-panel`
- `ladder_friends-bottom-panel ranking-bottom-panel`
- `season-reward-bottom-panel`
- `left-column-list-label`
- `middle-right-column-graphics`
- `right-column-background interface-element-middle-2-background-stretch`
- `search-wrapper search-in-left-column`
- `left-grouped-list-right-column right-column`
- `right-column-background interface-element-middle-1-background-stretch`
- `left-grouped-list-right-column-bottom-row-panel bottom-row-panel`
- `chat-input-wrapper`
- `chat-notification-wrapper`
- `chat-info-wrapper`
- `data-tip#info_tip#chat_lang`
- `chat-config-wrapper`
- `#chat_placeholder#chat_lang`
- `scroll-wrapper small-bar chat-message-wrapper`
- `chat-channel-card card`
- `chat-channel-card-icon`
- `chat-channel-not-read-counter`
- `chat-channel-card-wrapper tabs-nav`
- `new-chat-window`
- `chat-channel-card-wrapper`
- `chat-message-wrapper`
- `chat-configure-window`
- `#notifications#chat_lang`
- `#notifications_on_global_chat#chat_lang`
- `#formatting#chat_lang`
- `new-chat-message`
- `item-mini-map-icon`
- `outside-chat-mode-checkBox-wrapper`
- `.interface-layer>.right-column.main-column`
- `}]}}\`)},this.testInterfaceActionHideChatColumnButton=()=>{x(\`{`
- `}]}}\`)},this.testInterfaceActionShowChatColumnButton=()=>{x(\`{`
- `}]}}\`)},this.testInterfaceActionHideChatColumn=()=>{x(\`{`
- `}]}}\`)},this.testInterfaceActionShowChatColumn=()=>{x(\`{`
- `}]}}\`)},this.testInterfaceActionEqChatColumn=()=>{x(\`{`