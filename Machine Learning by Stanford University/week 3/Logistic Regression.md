Classification(분류)의 문제에 접근하는 방식 중 하나는 **`Binary Classification`**, 즉 **`0`**과 **`1`**로 구분 짓습니다. 
보통 **`Positive`**는 **`1`**, **`Negative`**는 **`0`**으로 정의합니다.

***

# 👤 Classification(Binary)에 대한 예시

다음은 강의에서 언급된 예시입니다.

  - Email : Spam / Not Spam
  - Online Transactions: Fraudulent (Yes / No)
  - Tumor : Malignant / Benign

아래 사진은 Tumor(종양)가 악성인지 아닌지에 대한 Binary Classification입니다.![image](https://user-images.githubusercontent.com/61633137/105687628-06b2f500-5f3c-11eb-9f99-6e5119447688.png) 

하지만 반드시 0과 1이 아닌 여러가지 값(1,2,3,4,...)으로 분류하는 것도 가능하다고 합니다. (자세한 내용은 다음 강의에)

<br>

***

Tumor 예시를 좀 더 살펴보겠습니다.

![image](https://user-images.githubusercontent.com/61633137/105689674-64e0d780-5f3e-11eb-8475-5def92af7773.png) 

위 첫 번째 그래프는 X축에 Tumor의 크기, Y축에는 악성종양 여부를 나타내고 있습니다.
여기에 분류 알고리즘을 적용시키려면 특정  **`Threshold`**값을 기준으로 잡아야 합니다.

![image](https://user-images.githubusercontent.com/61633137/105690931-f0a73380-5f3f-11eb-8497-cbf5e800ed05.png) 

두 번째 그래프는 Threshold $$h_\theta(x)$$를 $$0.5$$로 정한 그래프를 보여줍니다.
만약 $$h_\theta(x)$$가 0.5보다 크거나 같으면 $$y=1$$, 0.5보다 작으면 $$y=0$$으로 분류하는 것입니다.

하지만 분류 문제를 션형 회귀로 해결하는 것은 데이터에 좌지우지되는 경우가 많아서 좋은 접근법이 아닙니다.
그래서 앞으로 배울 **`Logistic Regression`**은 분류 문제를 해결할 수 있는 알고리즘입니다.

<br>

***

# 분류에 대한 Hypothesis Representation과 Sigmoid Function

분류 문제는 우리는 $$y$$가 discrete-value라는 것을 무시한 채로 접근할 수 있습니다.
또한 선형 회귀 알고리즘을 통해 주어진 $$x$$로 $$y$$를 예측해보려할 수도 있습니다.

하지만 이 방법은 예제에 따라 성능이 굉장히 떨어질 수 있습니다. 
$$y$$값이 0과 1중에 하나여야 한다는 것을 안다면 $$h_\theta(x)$$값이 1보다 크거나 0보다 작다는 것이 말이 되지 않는다는 것을 알 수 있습니다.

이러한 문제를 해결하기 위해 $$0 \leq h_\theta(x) \leq 1$$을 만족하는 가설 함수를 정의해보겠습니다.
$$
h_\theta(x) = g(\theta^Tx) \\
z = \theta^Tx \\
g(z) = \frac{1}{1+e^{-z}}
$$
위 가설 함수는 선형 회귀 함수의 값을 $$g$$함수로 감싼  **`Logistic Regression(로지스틱 회귀)`** 모델입니다.
이 새로운 함수를 **`Sigmoid Function(시그모이드 함수)`** 또는 **`Logistic Function(로지스틱 함수)`**라고도 합니다.
여기에 표시된 함수 $$g(z)$$는 임의의 값을 0~1 구간에 매핑하여 원래의 함수를 분류에 더 적합한 함수로 변환하는 데 유용합니다.

Sigmoid Function을 그래프로 그려보면 다음과 같이 0~1 사이의 값을 갖게 되는 그래프가 그려집니다.
![image](https://user-images.githubusercontent.com/61633137/105810343-1a1e9880-5fee-11eb-8b0d-64c66b40e17c.png)

여기서 $$h_\theta(x)$$는 결과가 1이 될 확률을 알려주게되며 이것은 0이 될 확률 또한 알려주게 됩니다.
예를 들어 $$h_\theta(x) = 0.7$$이라면 결과값이 1일 확률이 70%이며 0일 확률은 30%라는 의미입니다.

<br>

***

# 로지스틱 회귀를 이해하기 위한 결정 경계 

로지스틱 회귀의 $$h(x)$$가 0.5보다 크거나 같으면 $$y$$가 1이라고 예측하는 것으로 가정해보겠습니다.

아래 그래프에서 파란색 선은 로지스틱 함수, 
핑크색은 $$y$$가 1이라고 예측하기 위한 $$g(z)$$ ~ $$z$$의 범위,
빨간색은 $$y$$가 1이라고 예측하기 위한 $$g(z)$$ ~ $$z$$의 범위를 나타냅니다.

![image](https://user-images.githubusercontent.com/61633137/105819161-307f2100-5ffb-11eb-8133-fb2ea2efa953.png) 

그래프에 대해 더 설명해보자면 $$g(z)$$가 0.5보다 크거나 같기 위해서 $$z$$가 0보다 크거나 같아야 하며,
이말은 $$h(x) = g(\theta^Tx)$$에서 $$\theta^Tx$$가 0보다 크거나 같아야 한다는 의미입니다.

<br>

***

## Decision Boundary, 결정 경계

아래는 **`결정 경계`**를 알기위한 예시입니다.
![image](https://user-images.githubusercontent.com/61633137/105823479-8aceb080-6000-11eb-8fda-a44035b02793.png) 

![image](https://user-images.githubusercontent.com/61633137/105942388-7e9b2f80-60a2-11eb-833b-50300f8352ef.png)

$$\theta$$값을 각각 대입해주면 $$-3+x_1+x_2$$가 되고 이것이 0보다 크거나 같으면 $$y=1$$이라고 정의됩니다.
여기서 $$-3$$을 오른쪽으로 옮겨서 $$x_1+x_2 \geq 3, \ y=1$$ 이라고 나타낼 수 있습니다.
반대로 $$x_1+x_2 < 3$$이면 $$y=0$$이라고 할 수 있습니다.

그리고 $$x_1+x_2=3$$이면 $$h_\theta(x) = 0.5$$가 되는 것인데 이것이 바로 **`결정 경계`**입니다.
위 그래프에선 분홍색 선으로 표시되어 있습니다.

<br>

***

## Non-linear decision boundaries, 비선형 결정 경계

![image](https://user-images.githubusercontent.com/61633137/105824091-468fe000-6001-11eb-8302-2b5f2957740d.png) 

위 그래프에선 결정 경계를 어떻게 구할 수 있을까요?

우선 여기선 그래프에 원을 하나 그려봅니다.

![image](https://user-images.githubusercontent.com/61633137/105824388-9ec6e200-6001-11eb-85b0-74286e9ab50b.png) 

여기 분홍색 원의 바깥을 $$y=1$$, 안쪽을 $$y=0$$이라고 정의할 수 있겠습니다.
이것을 식으로 나타내보겠습니다.

![image](https://user-images.githubusercontent.com/61633137/105942441-97a3e080-60a2-11eb-96ed-cd7255381ea2.png)


$$x^2_1+x^2_2 \geq 1$$이면 $$y=1$$, 반대로 $$x^2_1+x^2_2 <1$$이면 $$y=0$$이라고 할 수 있습니다.

<br>

***

# 👤 로지스틱 회귀의 비용함수

**`로지스틱 회귀`**에서 파라미터 $$\theta$$를 최적화하기 위한 비용함수에 대해 알아보겠습니다.

> 비용함수가 무엇인지 모르겠다면 ➡ [머신러닝? 선형 회귀, 비용함수는 뭐고 경사하강법은 무엇인가요?](https://velog.io/@kwonhl0211/머신러닝-선형-회귀는-뭐고-비용함수는-무엇인가요)

설명에 앞서 수식들에 대해 정리를 해보겠습니다.

먼저 Training Set과 m의 예시입니다.
$$\{(x^{(1)},y^{(1)}),(x^{(2)},y^{(2)}),...,(x^{(m)},y^{(m)})\}$$
![image](https://user-images.githubusercontent.com/61633137/105946863-61b72a00-60ab-11eb-88d7-3e68400b9587.png)

로지스틱 함수입니다.
$$h_\theta(x) = \frac{1}{1+e^{-\theta^Tx}}$$

기존의 비용함수 수식입니다.
$$J(\theta)=\frac{1}{m}\sum^m_{i=1}\frac{1}{2}(h_\theta(x^{(i)})-y^{(i)})^2$$

이 비용함수는 **`선형 회귀`**에서 쓰이는데 **`로지스틱 회귀`**에선 조금 변형된 비용함수를 사용합니다. 

왜냐하면 로지스틱 함수는 결과값이 물결 모양을 그릴 것이며 많은 **`Local Optima`**을 만들 것이기 때문입니다. 

다시 말해 기존 비용함수는 로지스틱 회귀에서 **`볼록 함수(Convex Function)`**를 그리지 않고 다음과 같은 그래프를 그릴 것입니다.
![image](https://user-images.githubusercontent.com/61633137/105948907-2ae31300-60af-11eb-9c20-d0d380105eb7.png)


변형된 비용함수는 다음과 같습니다.
$$J(\theta)=\frac{1}{m}\sum^m_{i=1}Cost(h_\theta(x^{(i)}), y^{(i)})$$
만약 $$y=1$$이면, $$Cost(h_\theta(x), y)= -\log(h_\theta(x))$$
만약 $$y=0$$이면, $$Cost(h_\theta(x), y)= -\log(1-h_\theta(x))$$
![image](https://user-images.githubusercontent.com/61633137/105949224-b2308680-60af-11eb-83c2-3e36288fc21a.png)![image](https://user-images.githubusercontent.com/61633137/105948527-6df0b680-60ae-11eb-92d0-c92c87d76155.png)
그래프에 대해 추가 설명을 덧붙이자면
$$y=1$$일 때 $$h_\theta(x)$$가 0으로 예측되었다면 비용함수값은 무한대에 가까워지게 되는 것이고, 반대로 1로 예측되었다면 비용함수값은 0에 가까워지게 되는 것입니다.
$$y=0$$인 경우는 반대로 생각해보면 됩니다. 

<br>

***

## 비용함수 단순화와 로지스틱 회귀의 경사하강법

### Simplified Cost Function

위에서 살펴본 로지스틱 회귀에서의 비용함수는 어떻게 하나의 식으로 표현될 수 있는걸까요?

아래 수식이 $$y=1$$일 때와 $$0$$일 때의 수식을 합쳐서 표현한 로지스틱 비용함수입니다.
$$Cost(h_\theta(x), y)=-y\log(h_\theta(x))-(1-y)\log(1-h_\theta(x))$$

이에 대해 설명을 해보겠습니다.

$$y=1$$일 때는 $$-(1-y)\log(h_\theta(x))$$가 $$0$$이 되면서 남겨진 수식은 $$-1*\log(h_\theta(x))$$, 즉 $$-\log(h_\theta(x))$$가 되어 기존 $$y=1$$일 때의 수식이 됩니다.

$$y=0$$일 때는 $$-y\log(h_\theta(x))$$가 $$0$$이 되면서 남겨진 수식은 $$-(1-0)\log(1-h_\theta(x))$$, 즉 $$-\log(1-h_\theta(x))$$가 되어 기존 $$y=0$$일 떄의 수식이 됩니다.

<br>

***

### Gradient Descent

이전에 선형 회귀에서 배웠던 것처럼 로지스틱 회귀에서도 비용함수 $$J(\theta)$$를 최소로 하는 $$\theta$$값을 찾기 위해 경사하강법 알고리즘을 사용하게됩니다. 선형 회귀에서의 경사하강법 수식은 아래와 같습니다.

$$\begin{aligned} & Repeat \; \lbrace \\ & \; \theta_j := \theta_j - \alpha \dfrac{\partial}{\partial \theta_j}J(\theta) \\ & (simultaneously\ update\ all\ \theta_J )\\ & \rbrace \end{aligned}$$	

여기서 **`Learning Rate`**인 $$\alpha$$값 뒷부분을 로지스틱 함수로 바꾸면 됩니다.

$$\begin{aligned} & Repeat \; \lbrace \\ & \; \theta_j := \theta_j - \alpha \sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)}) x_j^{(i)} \\ & \rbrace \end{aligned}$$

<br>

***

## Advanced Optimization

경사하강법에서 비용함수를 최적의 $$\theta$$값을 구하려면 $$J(\theta)$$와 $$\frac{\partial}{\partial\theta_j}J(\theta)$$를 평가해야 합니다.

이 때 사용되는 방법은 경사하강법뿐만이 아닌 다른 방법들도 존재합니다.
- **`Conjugate Gradient`**
- **`BFGS`**
- **`L-BFGS`**

장점은 $$\alpha$$값을 직접 지정할 필요없으며 경사하강법보다 좋은 성능을 내는 경우도 있다는 것입니다.
단점으론 경사하강법보다 더 복잡하다는 것입니다.

강의에서 Andrew Ng 교수님은 나머지 알고리즘을 사용할 시 직접 구현하는 것보단 이미 존재하는 머신러닝 라이브러리를 활용하는 것을 추천하셨습니다.

<br>

***

# 👤 다중 분류 ONE vs ALL

이전 글 중에 **`Binary Classification`**, 즉 0과 1로 분류하는 것에 대해 대한 글이 있었습니다.

> 여기서 읽어보실 수 있습니다 ➡ [분류 문제와 결정 경계](https://velog.io/@kwonhl0211/분류-문제와-결정-경계)

이번엔 $$y$$가 $$0,1,2...n$$ 처럼 여러가지로 분류되는 **`Multiclass Classification`**에 대해서 알아보겠습니다. 

강의에선 이메일, 진단, 날씨를 예시로 들었는데요. 
그 중에 이메일의 경우 **`Work`**, **`Friends`**, **`Family`**, **`Hobby`**, 이렇게 4가지 태그로 분류한다고 정의하면 $$y=1$$~$$4$$의 값을 가진다고 볼 수 있습니다.

**`Binary Classification`**에선 결정 경계를 이용하여 분류하였습니다.
그렇다면 **`Multiclass Classfication`**에선 어떻게 분류할 수 있을까요?

제목에서 볼 수 있듯이 **`One vs All`**이라는 방식으로 접근합니다.(**`One vs Rest`**라고도 합니다.)

![image](https://user-images.githubusercontent.com/61633137/106232100-855aab80-6236-11eb-84da-47a1158a1f6f.png)

여기서 분류될 케이스를 각각 (1)세모, (2)네모, (3)엑스 모양으로 표시했습니다.
이것을 수식으로 나타내어보면 다음과 같이 정의할 수 있습니다.
$$h^{(i)}_\theta(x)=P(y=i|x;\theta) \ (i=1,2,3)$$

![image](https://user-images.githubusercontent.com/61633137/106232279-f7cb8b80-6236-11eb-8281-501e884a361a.png)

(1)세모의 경우 이에 해당하는 값만 $$y=1$$로 정의하고 그 외엔 모두 $$0$$으로 하는 것입니다. 그리고 이것을 결정 경계로 구분하며 이것을 반복합니다.

<br>

***

> Coursera에 있는 Andrew Ng 교수님의 Machine Learning 강의를 듣고 정리하는 시리즈입니다!

> 저의 수학 베이스가 부족하여 글의 내용이 틀릴 수도 있습니다. 잘못된 내용이 있을 시 댓글로 알려주시면 감사하겠습니다!!
> (수학 공부는 열심히 하고 있어요! 😁)