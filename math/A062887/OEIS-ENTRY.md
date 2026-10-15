# OEIS A062887 source capture

Accessed on 2026-10-15. The entry page response `Date` header was
`Thu, 15 Oct 2026 19:08:51 GMT` (UTC). The full text record and b-file were
fetched at `Thu, 15 Oct 2026 19:15:33 GMT` (UTC). The history page was fetched
at `Thu, 15 Oct 2026 19:10:11 GMT` (UTC).

- Entry page: <https://oeis.org/A062887>
- Full text record endpoint: <https://oeis.org/search?q=id:A062887&fmt=text>
- B-file: <https://oeis.org/A062887/b062887.txt> (saved verbatim as
  [`b062887.txt`](b062887.txt))
- History: <https://oeis.org/history?seq=A062887>

## Exact NAME line

`%N A062887 Smallest multiple of 2n+1 with the property that its digits are odd and each digit is two less (mod 10) than the previous digit, or 0 if no such number exists.`

## Conjecture comment, verbatim

`%C A062887 Conjecture: The only numbers n for which a(n)=0 are those for which 2*n+1 is divisible by 125. - _Sean A. Irvine_, Apr 14 2023`

## Full OEIS text record

The following is the full text record returned by the OEIS text endpoint. Field
codes and line contents are kept verbatim.

```text
# Greetings from The On-Line Encyclopedia of Integer Sequences! http://oeis.org/

Search: id:a062887
Showing 1-1 of 1

%I A062887 #12 Apr 14 2023 22:14:03
%S A062887 1,3,5,7,9,319,975,75,7531,19,197531975319,3197,75,5319,319,31,
%T A062887 3197531975319,53197531975,1975319,975,531975,1975319753197,
%U A062887 19753197531975,75319753197531,319753197531975319,753197531975319753
%N A062887 Smallest multiple of 2n+1 with the property that its digits are odd and each digit is two less (mod 10) than the previous digit, or 0 if no such number exists.
%C A062887 Conjecture: The only numbers n for which a(n)=0 are those for which 2*n+1 is divisible by 125. - _Sean A. Irvine_, Apr 14 2023
%e A062887 a(7) = 975 = 13*75 has decreasing odd digits.
%p A062887 l := 0:for i from 1 to 35 do for j from 1 to 5 do a := 0:for h from 1 to i do a := 10*a+((2*j+1-2*h) mod 10):end do:l := l+1:q[l] := a:end do:end do:s := seq(q[ll],ll=1..l); for i from 1 to 65 do k := 1:while((s[k] mod (2*i-1))>0) do k := k+1:end do: w[i] := s[k]:end do:seq(w[j],j=1..65);
%Y A062887 Cf. A062884, A062885.
%K A062887 nonn,base,easy
%O A062887 0,2
%A A062887 _Amarnath Murthy_, Jun 28 2001
%E A062887 More terms from _Sascha Kurz_, Mar 25 2002

# Content is available under The OEIS End-User License Agreement: http://oeis.org/LICENSE
```

## History check

The retrieved history page shows the conjecture comment as an added entry and
shows the status changing from `proposed` to `approved`. It contains no proof
or claim that the conjecture was already proved. This is a check of the
available page history, not a claim about unrecorded external sources.
