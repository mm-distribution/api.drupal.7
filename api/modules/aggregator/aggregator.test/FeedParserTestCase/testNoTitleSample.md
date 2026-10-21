# FeedParserTestCase::testNoTitleSample()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 1078–1084 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L1078-L1084)
- **Class:** [FeedParserTestCase](../FeedParserTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
function testNoTitleSample()
```

## Documentation

```text
Tests a feed with no title; the description should be used to generate one.
```

## Code

```php
  function testNoTitleSample() {
    $feed = $this->createFeed($this->getNoTitleSample());
    aggregator_refresh($feed);
    $this->drupalGet('aggregator/sources/' . $feed->fid);
    $this->assertResponse(200, format_string('Feed %name exists.', array('%name' => $feed->title)));
    $this->assertRaw("This description should be used to generate a title. This description should be used to generate a title. This description should be used to generate a title. This description should be used to generate a title. This description should be used to...");
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
