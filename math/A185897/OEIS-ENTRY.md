Fetched from https://oeis.org/A185897 on 2026-10-15T22:18:04+03:00.

The complete OEIS response follows verbatim, including the sequence entry and page markup.

```html

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html>
  
  <head>
  
  <link rel="stylesheet" href="/styles.css?v=20260826">
  <meta name="format-detection" content="telephone=no">
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <meta name=viewport content="width=device-width, initial-scale=1">
  <meta name="keywords" content="OEIS,integer sequences,Sloane" />
  
  
  
  <title>A185897 - OEIS</title>
  <link rel="search" type="application/opensearchdescription+xml" title="OEIS" href="/oeis.xml">
  
  <link rel="icon" type="image/svg+xml" href="/favicon.svg?v=20260826">
  <link rel="icon" sizes="16x16 32x32 48x48" href="/favicon.ico?v=20260826">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png?v=20260826">
  <script>
  var myURL = "\/A185897"
  function redir() {
      var host = document.location.hostname;
      if(host != "oeis.org" && host != "127.0.0.1" && !/^([0-9.]+)$/.test(host) && host != "localhost" && host != "localhost.localdomain") {
          document.location = "https"+":"+"//"+"oeis"+".org/" + myURL;
      }
  }
  function sf() {
      if(document.location.pathname == "/" && document.f) document.f.q.focus();
  }
  </script>
  </head>
  <body bgcolor=#ffffff onload="redir();sf()"><a href="https://oeis.org/cdn-cgi/content?id=js5G651KmcOmZN_L1Ma8bjcU_RpTB6t3VjaBi6t7WuQ-1792091817.8037715-1.2.1.1-J6IMGYWInGvZEqk5xDBuugRsBkrVWqM6ZsTTk3HyncfWvCDd6OfMzqe2rX3MYAyg" aria-hidden="true" rel="nofollow noopener" style="display: none !important; visibility: hidden !important"></a>
    <div class=loginbar>
      <div class=login>
      
        <a href="/login?redirect=%2FA185897" rel="nofollow">login</a>
      
      </div>
    </div>

    <div class=center><div class=top>
    <center>
    <div class=donors>
    The OEIS is supported by <a href="http://oeisf.org/#DONATE">the many generous donors to the OEIS Foundation</a>.
    </div>

    <div class=banner>
    <a href="/"><picture>
    <source media="(min-width: 830px)" srcset="/oeis-banner-wide.png 1x, /oeis-banner-wide@2x.png 2x" width="918" height="129">
    <img class=banner border="0" width="540" height="129" src="/oeis-banner.png" srcset="/oeis-banner.png 1x, /oeis-banner@2x.png 2x" alt="A185897 - OEIS">
    </picture></a>
    </div>

    
    
    
    <div class="motdbox" style="justify-content: center;">
        <div class="400k">
         <p>Nominations for sequence A400000 are open, see <a href="https://oeis.org/wiki/Nominations_for_Sequence_A400000">here</a>.</p>
        </div>
        
    </div>
    
    </center>
    </div></div>

    <div class=center><div class=pagebody>
      
    
    <div class=searchbarcenter>
        <form name=f action="/search" method="GET">
            <div class=searchbargreet>
                <div class=searchbar>
                    <div class=searchq>
                        <input class=searchbox maxLength=1024 name=q value="" title="Search Query">
                        
                        
                        
                        
                    </div>
                    <div class=searchsubmit>
                        <input type=submit value="Search" name=go>
                    </div>
                    <div class=hints>
                        <span class=hints><a href="/hints.html">Hints</a></span>
                    </div>
                </div>
                <div class=searchgreet>
                    (Greetings from <a href="/welcome">The On-Line Encyclopedia of Integer Sequences</a>!)
                </div>
            </div>
        </form>
    </div>

    <div class=sequence>
        <div class=space1></div>
        <div class=line></div>
        
        <div class=seqhead>
            <div class=seqnumname>
                <div class=seqnum>
                    
                        A185897
                    
                </div>
                <div class=seqname>
                    G.f. A(x) satisfies: A(x - A(x)^2) = x/(1-x).
                    
                </div>
            </div>
            <div class=scorerefs>
                        
                        2
            </div>
        </div>
        
            
    
    
    <div>
        <div class=seqdatabox>
            <div class=seqdata>1, 2, 9, 64, 574, 5919, 67205, 820258, 10602848, 143710500, 2028137178, 29649220223, 447247229447, 6940546801219, 110540089124381, 1803424905623166, 30092225956558590, 512900050694933194</div>
            
                <div class=seqdatalinks>
                (<a href="/A185897/list">list</a>;
                
                
                
                    <a href="/A185897/graph">graph</a>;
                
                <a rel=nofollow href="/search?q=A185897+-id:A185897">refs</a>;
                <a href="/A185897/listen">listen</a>;
                <a rel=nofollow href="/history?seq=A185897">history</a>;
                
                <a href="/search?q=id:A185897&fmt=text">text</a>;
                <a href="/A185897/internal">internal format</a>)
                </div>
            
        </div>
    </div>
    <div class=entry>
        
            
        
            
        
            
        
            
                 
                 
                 
                 
                     <div class=section>
                         <div class=sectname>OFFSET</div>
                         <div class=sectbody>
                             
                                 <div class=sectline>1,2</div>
                             
                         </div>
                     </div>
                 
            
        
            
                 
                 
                 
                 
                     <div class=section>
                         <div class=sectname>COMMENTS</div>
                         <div class=sectbody>
                             
                                 <div class=sectline>Conjecture: for n &gt; 1, a(n) is odd when n = 3*2^k through 4*2^k - 1 for k &gt;= 0. - <a href="/wiki/User:Paul_D._Hanna">Paul D. Hanna</a>, Oct 05 2025</div>
                             
                         </div>
                     </div>
                 
            
        
            
                 
                 
                 
                 
            
        
            
                 
                 
                 
                     
                 
                 
                     <div class=section>
                         <div class=sectname>LINKS</div>
                         <div class=sectbody>
                             
                                 <div class=sectline>Paul D. Hanna, <a href="/A185897/b185897.txt">Table of n, a(n) for n = 1..400</a></div>
                             
                         </div>
                     </div>
                 
            
        
            
                 
                 
                 
                 
                     <div class=section>
                         <div class=sectname>FORMULA</div>
                         <div class=sectbody>
                             
                                 <div class=sectline>G.f. A(x) = Sum_{n&gt;=1} a(n)*x^n and the related series G(x) (the g.f. of <a href="/A389476" title="G.f. A(x) satisfies: A( x - A(x)^2/(1 - A(x))^2 ) = x.">A389476</a>) satisfy the following formulas.</div>
                             
                                 <div class=sectline>(1) A(x - A(x)^2) = x/(1-x).</div>
                             
                                 <div class=sectline>(2) A(x) = G(x)/(1 - G(x)) where G(x - A(x)^2) = x.</div>
                             
                                 <div class=sectline>(3) G(x) = x + A(G(x))^2 where G(x) = Series_Reversion(x - A(x)^2).</div>
                             
                         </div>
                     </div>
                 
            
        
            
                 
                 
                 
                 
                     <div class=section>
                         <div class=sectname>EXAMPLE</div>
                         <div class=sectbody>
                             
                                 <div class=sectline>G.f.: A(x) = x + 2*x^2 + 9*x^3 + 64*x^4 + 574*x^5 + 5919*x^6 + 67205*x^7 + ...</div>
                             
                                 <div class=sectline>Related expansions.</div>
                             
                                 <div class=sectline>x - A(x)^2 = x - x^2 - 4*x^3 - 22*x^4 - 164*x^5 - 1485*x^6 - 15286*x^7 - ...</div>
                             
                                 <div class=sectline>where A(x - A(x)^2) = x/(1-x).</div>
                             
                                 <div class=sectline>Let G(x) be the g.f. of <a href="/A389476" title="G.f. A(x) satisfies: A( x - A(x)^2/(1 - A(x))^2 ) = x.">A389476</a>, which begins</div>
                             
                                 <div class=sectline>G(x) = x + x^2 + 6*x^3 + 47*x^4 + 442*x^5 + 4691*x^6 + 54330*x^7 + 672992*x^8 + ... + <a href="/A389476" title="G.f. A(x) satisfies: A( x - A(x)^2/(1 - A(x))^2 ) = x.">A389476</a>(n)*x^n + ...</div>
                             
                                 <div class=sectline>then A(x) = G(x)/(1 - G(x)) and G(x - A(x)^2) = x.</div>
                             
                         </div>
                     </div>
                 
            
        
            
                 
                 
                 
                 
            
        
            
                 
                 
                 
                 
            
        
            
                 
                 
                 
                 
                     <div class=section>
                         <div class=sectname>PROG</div>
                         <div class=sectbody>
                             
                                 <div class=sectline>(PARI) {a(n) = my(A=x+2*x^2, B=x/(1+x+x*O(x^n))); for(i=1, n, A=serreverse(B - subst(A, x, B)^2)); polcoef(A, n)}</div>
                             
                                 <div class=sectline>for(n=1, 25, print1(a(n), &quot;, &quot;))</div>
                             
                         </div>
                     </div>
                 
            
        
            
                 
                 
                     
                 
                 
                 
                     <div class=section>
                         <div class=sectname>CROSSREFS</div>
                         <div class=sectbody>
                             
                                 <div class=sectline>Cf. <a href="/A389476" title="G.f. A(x) satisfies: A( x - A(x)^2/(1 - A(x))^2 ) = x.">A389476</a>, <a href="/A213591" title="G.f. A(x) satisfies A( x - A(x)^2 ) = x.">A213591</a>.</div>
                             
                                 <div class=sectline>Sequence in context: <a href="/A289717" title="The order of the semigroup of orientation-preserving or reserving partial transformations of n elements.">A289717</a> <a href="/A381908" title="Expansion of (1/x) * Series_Reversion( x / ((1+x) * B(x)) ), where B(x) is the g.f. of A002293.">A381908</a> <a href="/A094100" title="Fit a polynomial of degree k-1 to column k of array in A048790, evaluate it at dimension n = -1.">A094100</a> * <a href="/A067297" title="Convolution of C(2,2; n) := A064340(n) (generalized Catalan numbers) with itself.">A067297</a> <a href="/A274394" title="E.g.f. A(x) satisfies: A( A( x^4*exp(-4*x) )^(1/4) ) = x.">A274394</a> <a href="/A368291" title="Expansion of e.g.f. exp(x) / (1 - x*exp(2*x)).">A368291</a></div>
                             
                                 <div class=sectline>Adjacent sequences:  <a href="/A185894" title="a(n) = A001222(A027623(n)).">A185894</a> <a href="/A185895" title="Exponential generating function is (1-x^1/1!)(1-x^2/2!)(1-x^3/3!)....">A185895</a> <a href="/A185896" title="Triangle of coefficients of (1/sec^2(x))*D^n(sec^2(x)) in powers of t = tan(x), where D = d/dx.">A185896</a> * <a href="/A185898" title="G.f. satisfies: x + x^2 = A(x - A(x)^2).">A185898</a> <a href="/A185899" title="1/8 the number of n X 2 0..7 arrays with every element equal to exactly one or two of its horizontal and vertical neighbors.">A185899</a> <a href="/A185900" title="1/8 the number of nX3 0..7 arrays with every element equal to exactly one or two of its horizontal and vertical neighbors.">A185900</a></div>
                             
                         </div>
                     </div>
                 
            
        
            
                 
                 
                 
                 
                     <div class=section>
                         <div class=sectname>KEYWORD</div>
                         <div class=sectbody>
                             
                                 <div class=sectline><span title="a sequence of nonnegative numbers">nonn</span></div>
                             
                         </div>
                     </div>
                 
            
        
            
                 
                 
                 
                 
                     <div class=section>
                         <div class=sectname>AUTHOR</div>
                         <div class=sectbody>
                             
                                 <div class=sectline><a href="/wiki/User:Paul_D._Hanna">Paul D. Hanna</a>, Feb 05 2011</div>
                             
                         </div>
                     </div>
                 
            
        
            
                 
                 
                 
                 
                     <div class=section>
                         <div class=sectname>EXTENSIONS</div>
                         <div class=sectbody>
                             
                                 <div class=sectline>Entry revised by <a href="/wiki/User:Paul_D._Hanna">Paul D. Hanna</a>, Oct 05 2025</div>
                             
                         </div>
                     </div>
                 
            
        
            
                 
                 
                 
                 
                     <div class=section>
                         <div class=sectname>STATUS</div>
                         <div class=sectbody>
                             
                                 <div class=sectline>approved</div>
                             
                         </div>
                     </div>
                 
            
        

        
    </div>

        
        <div class=space10></div>
    </div>

    </div></div>

    <p>

    <div class=footerpad></div>
    <div class=footer>
    <center>
    <div class=bottom>
    <div class=linksbar>
      <a href="/">Lookup</a>
      <a href="/wiki/Welcome"><font color="red">Welcome</font></a>
      <a href="/wiki/Main_Page"><font color="red">Wiki</font></a>
      <a href="/account">Register</a>
      
      <a href="/play.html">Music</a>
      <a href="/plot2.html">Plot 2</a>
      <a href="/demo1.html">Demos</a>
      <a href="/wiki/Index_to_OEIS">Index</a>
      <a href="/webcam">WebCam</a>
      <a href="/Submit.html">Contribute</a>
      <a href="/eishelp2.html">Format</a>
      <a href="/wiki/Style_Sheet">Style Sheet</a>
      <a href="/transforms.html">Transforms</a>
      <a href="/ol.html">Superseeker</a>
      <a href="/recent">Recents</a>
    </div>
    <div class=linksbar>
      <a href="/community.html">The OEIS Community</a>
    </div>
    <div class=linksbar>
      Maintained by <a href="http://oeisf.org">The OEIS Foundation Inc.</a>
    </div>

    <div class=dbinfo>Last modified October 15 15:16 EDT 2026.  Contains 400327 sequences.</div>
    <div class=legal>
    <a href="/wiki/Legal_Documents">License Agreements, Terms of Use, Privacy Policy</a>
    </div>

    </div>
    </center>
    </div>
  <script>(function(){function c(){var b=a.contentDocument||(a.contentWindow&&a.contentWindow.document);if(b){var d=b.createElement('script');d.innerHTML="window.__CF$cv$params={r:'a4b1294548ffd784',t:'MTc5MjA5MTgxNw=='};var a=document.createElement('script');a.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js';document.getElementsByTagName('head')[0].appendChild(a);";b.getElementsByTagName('head')[0].appendChild(d)}}if(document.body){var a=document.createElement('iframe');a.height=1;a.width=1;a.style.position='absolute';a.style.top=0;a.style.left=0;a.style.border='none';a.style.visibility='hidden';document.body.appendChild(a);if('loading'!==document.readyState)c();else if(window.addEventListener)document.addEventListener('DOMContentLoaded',c);else{var e=document.onreadystatechange||function(){};document.onreadystatechange=function(b){e(b);'loading'!==document.readyState&&(document.onreadystatechange=e,c())}}}})();</script></body>
</html>
```
