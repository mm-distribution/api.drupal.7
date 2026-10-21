# FeedParserTestCase::testAtomSample()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 1053–1062 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L1053-L1062)
- **Class:** [FeedParserTestCase](../FeedParserTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
function testAtomSample()
```

## Documentation

```text
Tests a feed that uses the Atom format.
```

## Code

```php
  function testAtomSample() {
    $feed = $this->createFeed($this->getAtomSample());
    aggregator_refresh($feed);
    $this->drupalGet('aggregator/sources/' . $feed->fid);
    $this->assertResponse(200, format_string('Feed %name exists.', array('%name' => $feed->title)));
    $this->assertText('Atom-Powered Robots Run Amok');
    $this->assertLinkByHref('http://example.org/2003/12/13/atom03');
    $this->assertText('Some text.');
    $this->assertEqual('urn:uuid:1225c695-cfb8-4ebb-aaaa-80da344efa6a', db_query('SELECT guid FROM {aggregator_item} WHERE link = :link', array(':link' => 'http://example.org/2003/12/13/atom03'))->fetchField(), 'Atom entry id element is parsed correctly.');
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
