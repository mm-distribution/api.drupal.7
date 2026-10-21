# FeedParserTestCase::testHtmlEntitiesSample()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 1067–1073 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L1067-L1073)
- **Class:** [FeedParserTestCase](../FeedParserTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
function testHtmlEntitiesSample()
```

## Documentation

```text
Tests a feed that uses HTML entities in item titles.
```

## Code

```php
  function testHtmlEntitiesSample() {
    $feed = $this->createFeed($this->getHtmlEntitiesSample());
    aggregator_refresh($feed);
    $this->drupalGet('aggregator/sources/' . $feed->fid);
    $this->assertResponse(200, format_string('Feed %name exists.', array('%name' => $feed->title)));
    $this->assertRaw("Quote&quot; Amp&amp;");
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
