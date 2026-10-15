# Primary sources

Accessed 2026-10-15. The PDFs that were obtained are in [`sources/`](sources/).

## A. Erdős, “Some of my forgotten problems in number theory” (1992)

**Full text:** [Hardy–Ramanujan Journal 15 (1992), 34–50](https://hrj.episciences.org/125), PDF URL: <https://hrj.episciences.org/125/pdf>. DOI: <https://doi.org/10.46298/hrj.1992.125>. Saved as [`sources/erdos-1992-forgotten-problems.pdf`](sources/erdos-1992-forgotten-problems.pdf).

The following is a verbatim transcription of the relevant printed text (pp. 34–35). Line breaks and mathematical layout are normalized; words and formulas are retained.

> First of all let me state a completely forgotten problem of Surányi and myself [1]. Gallai noticed that one can find three integers \(a_1<a_2<a_3\) for which there are \(a_3\) consecutive integers \(0<x+1,x+2,\ldots,x+a_3\) the product of no three of which is a multiple of \(a_1a_2a_3\), but for every two integers \(1\leq a_1<a_2\) one can find among any \(a_2\) consecutive integers two of them whose product is a multiple of \(a_1a_2\). This was posed as a problem in a Hungarian competition. Surányi and I investigated the general situation.
>
> Let \(g(n)\) be the smallest integer for which if \(1<a_1<a_2<\cdots<a_n\) is any sequence of \(n\) integers then for every \(x\geq0\) we can find \(g(n)\) integers among \(x+1,x+2,\ldots,x+a_n\) whose product is a multiple of \(\prod_{i=1}^n a_i\), i.e. there are integers \(x<u_1<u_2<\cdots<u_{g(n)}\leq x+a_n\) for which \(\prod_{i=1}^{g(n)}u_i\equiv0\pmod{\prod_{i=1}^n a_i}\). We proved \(g(3)=4\) and proved that for every \(\epsilon>0\) there is an \(n_0\) so that for every \(n>n_0\)
>
> \[
> g(n)>(2-\epsilon)n. \tag{1}
> \]
>
> Since our paper only appeared in Hungarian we outline the proof of (1) here. Let \(p_1<p_2<\cdots<p_\ell\) be a set of \(\ell\) primes satisfying \(2p_1^2>p_\ell^2\). Using the Chinese remainder theorem it is easy to find \(p_\ell^2\) consecutive integers \(x+1,\ldots,x+p_\ell^2\) for which \(x+\left[\frac{p_\ell^2}{2}\right]\equiv0\pmod{\prod_{i=1}^{\ell}p_i\!}\) but \(x+\left[\frac{p_\ell^2}{2}\right]\not\equiv0\pmod{p_i^2}\), also none of the integers \(x+t\), \(1\leq t\leq p_\ell^2\) (\(t\ne[\frac{p_\ell^2}{2}]\)) are divisible by any of the \(p_ip_j\), \(1\leq i<j\leq\ell\), and none of the integers \(x+t\) are multiples of \(p_i^3\) and only one of them is a multiple of \(p_i^2\). Our \(a_i\) are the \(\binom{\ell+1}{2}\) integers \(p_ip_j\), \(1\leq i\leq j\leq\ell\). Clearly
>
> \[
> \prod a_i=\left(\prod_{i=1}^{\ell}p_i\right)^{\ell+1}.
> \]
>
> Now by a simple computation (the details of which can be left to the reader) the product of \((2-\epsilon)\binom{\ell+1}{2}\) integers \(x+t\), \(1\leq t\leq p_\ell^2\) is never a multiple of \(\left(\prod_{i=1}^{\ell}p_i\right)^{\ell+1}\).

The statement at the start of the next paragraph is verbatim: “Now we asked: Is it true that \(g(n)<(2+\epsilon)n\) or perhaps even \(g(n)\leq2n\).”

The two-number result above implies \(g(2)=2\) under this definition: it gives the upper bound 2, and the requirement that two distinct integers be selected gives the lower bound 2. This value is an implication of the text, not a separately printed equation. The paper states \(g(3)=4\) explicitly.

The interval-length variant and its printed values (p. 35) are verbatim:

> We further asked: What is the smallest \(c_n\geq1\) so that among any \(c_na_n\) consecutive integers one can always find \(n\) of them whose product is a multiple of \(\prod_{i=1}^n a_i\). Then \(c_2=1\) and we proved \(c_3=\sqrt2\), we have no good upper or lower bounds for \(c_n\).

## B. Erdős and Surányi, “Megjegyzések egy versenyfeladathoz” (1959)

**Full text:** Rényi Institute archive, file URL <https://users.renyi.hu/~p_erdos/1959-07.pdf>. The archive index is <https://users.renyi.hu/~p_erdos/Erdos.html>. This is the scan of *Matematikai Lapok* 10 (1959), 39–48, saved as [`sources/erdos-suranyi-1959-mat-lapok-10-39-48.pdf`](sources/erdos-suranyi-1959-mat-lapok-10-39-48.pdf). It includes the Hungarian article and German and Russian abstracts.

### Section 1: original statement and answer for two and three inputs

Verbatim Hungarian (p. 39; spacing normalized, mathematical symbols retained):

> Ismeretes, hogy az 1, 2, ..., k számok szorzatával bármely egymásutáni k szám szorzata osztható. GALLAI Tibortól származik az a kérdés, hogy ha tetszésszerint adunk meg különböző egészeket és annyi egymásutáni egész számot, mint az adott számok legnagyobbika, akkor hány számot kell ezek közül kiválasztani, hogy a kiválasztott számok szorzata már minden esetben osztható legyen az adott számok szorzatával. Speciálisan 2 és 3 számra a következő kérdés adódik — és ez versenyfeladatként szerepelt: Döntsük el a következő állítások helyességét: a) Ha \(a>b\) pozitív egész számok, akkor bármely \(b\) számú egymásután következő egész szám között van két olyan, amelyek szorzata osztható \(ab\)-vel. b) Ha \(a<b<c\) pozitív egész számok, akkor bármely \(c\) számú egymásután következő egész szám között van három olyan, amelyek szorzata osztható \(abc\)-vel. A válasz az a) kérdésre igenlő, a b) kérdésre viszont pl. \(a=7\cdot11,b=7\cdot13,c=11\cdot13\) és a \((6\cdot7\cdot11\cdot13-71=)5935\ldots6077(=6\cdot7\cdot11\cdot13+71)\) számköz ellenpéldát szolgáltat.

**Literal translation (our translation):**

> It is known that the product of any \(k\) consecutive numbers is divisible by the product of the numbers \(1,2,\ldots,k\). The question comes from Tibor Gallai: if distinct integers are given at will, and as many consecutive integers as the greatest of the given numbers, how many of these must be selected so that the product of the selected numbers is in every case divisible by the product of the given numbers? In particular, for 2 and 3 numbers the following question arises—and it appeared as a competition problem: Decide whether the following statements are correct: a) If \(a>b\) are positive integers, then among any \(b\) consecutive integers there are two whose product is divisible by \(ab\). b) If \(a<b<c\) are positive integers, then among any \(c\) consecutive integers there are three whose product is divisible by \(abc\). The answer to a) is affirmative; for b), however, for example \(a=7\cdot11,b=7\cdot13,c=11\cdot13\) and the interval \((6\cdot7\cdot11\cdot13-71=)5935\ldots6077(=6\cdot7\cdot11\cdot13+71)\) supply a counterexample.

The scan’s displayed counterexample interval endpoints are 5935 and 6077. The ellipsis above represents consecutive integers between those endpoints; the printed article’s typography uses a dash-like separator.

### Section 9: lower-bound construction

Verbatim Hungarian (p. 44; line breaks normalized):

> Az így nyert ellenpéldákban \(k\) szám megadása esetén \(k+1\) szám kiválasztása mindig elegendő, általában azonban ennél sokkal rosszabb is lehet a helyzet. Vegyünk \(\ell\) prímszámot: \(p_1<p_2<\cdots<p_\ell\) úgy, hogy \(2p_1^2\) nagyobb legyen, mint \(p_\ell^2\). Ez tetszésszerinti \(\ell\)-re lehetséges, mivel a szomszédos prímek hányadosa 1-hez tart. Képezzük az összes \(p_ip_j\) (\(i,j=1,\ldots,\ell\)) számokat. Ezek száma \(k=\ell(\ell+1)/2\). Találhatunk olyan \(p_\ell^2\) egymásutáni számot, amelyek között előfordul \(p_1,p_2,\ldots,p_\ell\) egy többszöröse, amely ezen prímek egyikének a négyzetével sem osztható, ezen kívül nem fordul elő a \(p_ip_j\) (\(i,j=1,\ldots,\ell;\ i\ne j\)) többszöröse. Végül \(p_1^2,p_2^2,\ldots,p_\ell^2\)-nek csak egy-egy többszöröse fordul elő, de ezek sem oszthatók a megfelelő \(p_i\)-nek 2-nél magasabb kitevős hatványával. Ilyen számköz a \(2p_1^2>p_\ell^2\) feltétel következtében alkalmas kongruenciák megoldásával megadható.
>
> Az adott számok szorzata \(p_1^{\ell+1}p_2^{\ell+1}\cdots p_\ell^{\ell+1}\). Kiválasztva a több, \(p_i\)-vel, vagy valamelyik \(p_i\)-nek magasabb hatványával osztható számokat, ezek száma \(\ell+1\) és szorzatuk az adott prímek mindegyikének a köbével osztható. Minden további prímtényezőhöz tehát már egy-egy külön szám kiválasztása szükséges, összesen \(\ell(\ell-2)\)-é, az előbbi \(\ell+1\) számmal együtt \(\ell(\ell-1)+1\) számot kell tehát a kérdéses számközből kiválasztani, hogy szorzatuk osztható legyen az adott \(\ell(\ell+1)/2\) szám szorzatával. Itt tehát a kiválasztandó számok száma közel kétszerese az adottakénak. Azt nem tudjuk, hogy lehet-e ez az arány lényegesen kedvezőtlenebb is.

**Literal translation (our translation):**

> In the counterexamples obtained in this way, when \(k\) numbers are given, selecting \(k+1\) numbers is always sufficient; in general, however, the situation can be much worse. Take \(\ell\) primes \(p_1<p_2<\cdots<p_\ell\) such that \(2p_1^2\) is greater than \(p_\ell^2\). This is possible for arbitrary \(\ell\), since the ratios of consecutive primes tend to 1. Form all the numbers \(p_ip_j\) (\(i,j=1,\ldots,\ell\)). Their number is \(k=\ell(\ell+1)/2\). We can find \(p_\ell^2\) consecutive numbers among which there occurs a multiple of one of \(p_1,p_2,\ldots,p_\ell\) that is not divisible by the square of any of these primes; in addition, no multiple of \(p_ip_j\) (\(i,j=1,\ldots,\ell; i\ne j\)) occurs. Finally, only one multiple of each of \(p_1^2,p_2^2,\ldots,p_\ell^2\) occurs, and these are not divisible by a power of the corresponding \(p_i\) with exponent greater than 2. Such an interval can be given by solving suitable congruences, because of the condition \(2p_1^2>p_\ell^2\).
>
> The product of the given numbers is \(p_1^{\ell+1}p_2^{\ell+1}\cdots p_\ell^{\ell+1}\). Selecting the numbers divisible by more than one \(p_i\), or by a higher power of some \(p_i\), gives \(\ell+1\) numbers, and their product is divisible by the cube of each of the given primes. Thus, for every further prime factor one more separate number must be selected, \(\ell(\ell-2)\) in total. Together with the preceding \(\ell+1\) numbers, one must therefore select \(\ell(\ell-1)+1\) numbers from the interval for their product to be divisible by the product of the given \(\ell(\ell+1)/2\) numbers. Thus the number of selected numbers is close to twice the number given. We do not know whether this ratio can be considerably worse.

The printed counting formula \(k=\ell(\ell+1)/2\), and the following product formula, require the set of distinct products to include \(p_i^2\). This is also explicit in the 1992 English restatement, \(1\leq i\leq j\leq\ell\). The 1959 sentence “all \(p_ip_j\)” does not itself spell out an ordering of the indices.

### Section 10: distinct-multiple variant

Verbatim Hungarian (p. 45, formulas displayed inline):

> Egy további rokon probléma a következő: \(f(n)\) jelentse azt a legkisebb számot, amely mellett igaz, hogy bárhogy adunk is meg \(n\) különböző természetes számot \(a_1<a_2<\cdots<a_n\), tetszésszerinti \(f(n)a_n\) egymásutáni egész szám közül kiválasztható \(n\) szám úgy, hogy köztük minden \(a_i\)-nek szerepeljen többszöröse és különböző \(a_i\)-khez kiválasztott többszörösök különbözők legyenek. Meghatározandó \(f(n)\).

**Literal translation (our translation):**

> A further related problem is this: let \(f(n)\) denote the smallest number such that, however \(n\) distinct natural numbers \(a_1<a_2<\cdots<a_n\) are given, from any \(f(n)a_n\) consecutive integers one can select \(n\) numbers so that there is among them a multiple of every \(a_i\), and the multiples selected for different \(a_i\)'s are different. Determine \(f(n)\).

This is the source’s distinct-multiple condition. It is introduced as a different, related function, after the \(g(n)\) problem.

## C. Erdős, “Some unsolved problems in geometry, number theory and combinatorics” (Eureka 52 (1992), 44–48)

Bibliographic entry as given by the problem database: *Eureka* 52 (1992), 44–48. The Archimedeans publications page is <https://archim.org.uk/publications/>. Its “Eureka Archives” link points to <https://1drv.ms/f/s!ApvGm4MgQBO_gRJuB2QJqRw9H0lr?e=tyhSXE>.

I did not obtain the Eureka PDF. The current Archimedeans site exposes the archive through that OneDrive folder, which returned HTTP 403 in this session. The requested exact-title search in the Internet Archive returned no matching item; the Internet Archive CDX requests timed out. Direct guesses at the Archimedeans’ old `/eureka/` PDF paths returned 404. Therefore I do not quote or rely on this item for the statement reconciliation. The two obtainable primary sources above provide direct text for the issue under review.
