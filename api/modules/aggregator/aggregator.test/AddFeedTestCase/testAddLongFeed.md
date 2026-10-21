# AddFeedTestCase::testAddLongFeed()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 385–409 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L385-L409)
- **Class:** [AddFeedTestCase](../AddFeedTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
function testAddLongFeed()
```

## Documentation

```text
Tests feeds with very long URLs.
```

## Code

```php
  function testAddLongFeed() {
    // Create a feed with a URL of > 255 characters.
    $long_url = "https://www.google.com/search?ix=heb&sourceid=chrome&ie=UTF-8&q=angie+byron#sclient=psy-ab&hl=en&safe=off&source=hp&q=angie+byron&pbx=1&oq=angie+byron&aq=f&aqi=&aql=&gs_sm=3&gs_upl=0l0l0l10534l0l0l0l0l0l0l0l0ll0l0&bav=on.2,or.r_gc.r_pw.r_cp.,cf.osb&fp=a70b6b1f0abe28d8&biw=1629&bih=889&ix=heb";
    $feed = $this->createFeed($long_url);

    // Create a second feed of > 255 characters, where the only difference is
    // after the 255th character.
    $long_url_2 = "https://www.google.com/search?ix=heb&sourceid=chrome&ie=UTF-8&q=angie+byron#sclient=psy-ab&hl=en&safe=off&source=hp&q=angie+byron&pbx=1&oq=angie+byron&aq=f&aqi=&aql=&gs_sm=3&gs_upl=0l0l0l10534l0l0l0l0l0l0l0l0ll0l0&bav=on.2,or.r_gc.r_pw.r_cp.,cf.osb&fp=a70b6b1f0abe28d8&biw=1629&bih=889";
    $feed_2 = $this->createFeed($long_url_2);

    // Check feed data.
    $this->assertTrue($this->uniqueFeed($feed->title, $feed->url), 'The first long URL feed is unique.');
    $this->assertTrue($this->uniqueFeed($feed_2->title, $feed_2->url), 'The second long URL feed is unique.');

    // Check feed source.
    $this->drupalGet('aggregator/sources/' . $feed->fid);
    $this->assertResponse(200, 'Long URL feed source exists.');
    $this->assertText($feed->title, 'Page title');
    $this->drupalGet('aggregator/sources/' . $feed->fid . '/categorize');
    $this->assertResponse(200, 'Long URL feed categorization page exists.');

    // Delete feeds.
    $this->deleteFeed($feed);
    $this->deleteFeed($feed_2);
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
