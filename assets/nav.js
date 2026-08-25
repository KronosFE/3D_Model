/* Kronos Model — unified topnav (Machine · Physics · Program · Lab)
   Renders into <nav class="topnav" id="kfe-nav">. Path-aware from its own src. */
(function(){
"use strict";
var s=document.querySelector('script[src*="nav.js"]');
var BASE=new URL(s.getAttribute('src'),location.href).href.replace(/assets\/nav\.js.*$/,'');
var here=location.href.split('#')[0].split('?')[0];

var SECTIONS=[
  {key:'home',    label:'Overview', href:'index.html'},
  {key:'machine', label:'Machine',  href:'machine/index.html', sub:[
      ['Overview','machine/index.html'],['3D Reactor','machine/reactor-3d.html'],
      ['Hardware & Systems','machine/hardware.html'],['Materials & Environment','machine/materials.html'],
      ['Instructional film','instructional_video.html']]},
  {key:'physics', label:'Physics',  href:'physics/index.html', sub:[
      ['Governing Physics','physics/index.html'],['Breeder','physics/breeder.html'],
      ['Burner','physics/burner.html'],['Reactivity','physics/reactivity.html'],['Blanket','physics/blanket.html'],['Divertor','physics/divertor.html'],['Core turbulence','physics/turbulence.html'],['Magnets','physics/magnets.html'],
      ['Validation & UQ','physics/validation.html'],
      ['Environment','physics/environment.html'],['Deposits','physics/deposits.html']]},
  {key:'program', label:'Program',  href:'program/index.html', sub:[
      ['Overview','program/index.html'],['Roadmap','program/roadmap.html'],
      ['Readiness & Risks','program/readiness.html'],['Computing','program/computing.html'],
      ['About the Record','program/about.html']]},
  {key:'lab',     label:'Lab',      href:'lab/index.html'}
];

function abs(p){return new URL(p,BASE).href;}
function cur(sec){
  if(sec.key==='home')return here===abs('index.html')||here===BASE;
  if(here===abs(sec.href))return true;
  var dir=abs(sec.href).replace(/index\.html$/,'');
  return here.indexOf(dir)===0;
}

var nav=document.getElementById('kfe-nav');
if(nav){
  var active=null;
  var links=SECTIONS.map(function(sec){
    var on=cur(sec); if(on&&sec.key!=='home')active=sec; else if(on&&!active)active=sec;
    return '<a href="'+abs(sec.href)+'"'+(on?' class="on"':'')+'>'+sec.label+'</a>';
  }).join('');
  var html='<div class="in">'+
    '<a class="mark" href="'+abs('index.html')+'" style="color:inherit"><span class="orb"></span>'+
    '<span><b>KRONOS</b>&nbsp;MODEL</span></a>'+
    '<div class="navlinks">'+links+'</div>'+
    '<a class="doi-pill" href="'+abs('physics/deposits.html')+'">OPEN DEPOSITS · <b>CC BY 4.0</b></a>';
  if(active&&active.sub){
    html+='<div class="subnav"><span class="seclabel">'+active.label+'</span>'+
      active.sub.map(function(it){
        var on=here===abs(it[1]);
        return '<a href="'+abs(it[1])+'"'+(on?' class="on"':'')+'>'+it[0]+'</a>';
      }).join('')+'</div>';
  }
  html+='</div>';
  nav.innerHTML=html;
}
})();
