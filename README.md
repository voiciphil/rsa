# RSA

어떤 큰 수를 소인수분해하기 어렵다는 전제 하에 발명된 공개키 암호화 기법이다.

## 키 생성
1. 임의의 서로 다른 큰 소수 p, q를 선택한다.
2. `N := p * q`를 계산한다.
3. `phi(N)` 보다 작은 임의의 양의 정수 `e`를 선택한다. (`phi`는 Euler phi function이고, `gcd(phi(N), e) = 1`을 만족해야한다.)
4. `(e * d) % phi(N) = 1`을 만족하는 `d`를 계산한다.
5. 공개키 `pk := (N, e)`, 비밀키 `sk := d`를 계산한다.
6. 출력: `(pk, sk)`

## 암호화
0. 입력: 암호화할 메세지 `M` (`M`은 `N`보다 작은 0 이상의 정수이다.), 공개키 `pk`
1. `(N, e) := pk`
1. 출력: 암호화된 메세지 `C := M^e % N`

## 복호화
0. 입력: 암호화된 메세지 `C`, 비밀키 `sk`, `N`
1. `d := sk`
2. 출력: 복호화된 메세지 `M := C^d % N`

## 검증
Euler's Theorem을 사용해 `Dec(sk, N, Enc(pk, M)) = M`임을 증명한다.
```
Dec(sk, N, Enc(pk, M)) 
= M^(e * d) % N
= M^(k * phi(N) + 1) % N
= ((M^phi(N) % N)^k % N) * (M % N)
= (1^k % N) * (M % N)
= M
```
