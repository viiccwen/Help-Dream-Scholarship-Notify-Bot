# 圓夢助學網獎學金通知機器人

![](https://imgur.com/7MvRzU8.jpg)

---

> Based on `python`, `telegram bot`, `GitHub Action`

## 緣由 Origin
由於要申請獎學金，但有時候一忙就好幾天沒看，而且有的獎學金又期限很短，常常一個禮拜沒看就錯失一個機會，所以才有這東東的誕生。

## 困難 Difficulty
### Telegram Bot
由於`telegram bot`相對冷門，所以只能自己去翻docs慢慢拼程式QQ，寫程式時間大概只有10mins，看docs+嘗試卻花四五小時。

### GCP (Google Cloud Platform)
原本想說架在Google Cloud Platform，用Cloud Function跟Cloud Scheduler完成cronjob，但也是一直卡，用了六七個小時，最後只好含淚放棄QWQ，等我知識點到了再去接觸。

## 更新 Updates
### v0.0.1 ~ v0.0.2
嘗試不同寫法、修正程式清晰度
### v0.0.3
加入`Github Action`，在每天8:00 A.M.會自動推播
> 但`Github Action`存在延遲，通常會在9:14 A.M.左右推播

### v0.0.4
沒注意到字串中的`&`會導致URL送request被切斷，已修正

