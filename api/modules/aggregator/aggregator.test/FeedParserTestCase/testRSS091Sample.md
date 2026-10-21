# FeedParserTestCase::testRSS091Sample()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 1031–1048 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L1031-L1048)
- **Class:** [FeedParserTestCase](../FeedParserTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
function testRSS091Sample()
```

## Documentation

```text
Tests a feed that uses the RSS 0.91 format.
```

## Code

```php
  function testRSS091Sample() {
    $feed = $this->createFeed($this->getRSS091Sample());
    aggregator_refresh($feed);
    $this->drupalGet('aggregator/sources/' . $feed->fid);
    $this->assertResponse(200, format_string('Feed %name exists.', array('%name' => $feed->title)));
    $this->assertText('First example feed item title');
    $this->assertLinkByHref('http://example.com/example-turns-one');
    $this->assertText('First example feed item description.');

    // Several additional items that include elements over 255 characters.
    $this->assertRaw("Second example feed item title.");
    $this->assertText('Long link feed item title');
    $this->assertText('Long link feed item description');
    $this->assertLinkByHref('http://example.com/tomorrow/and/tomorrow/and/tomorrow/creeps/in/this/petty/pace/from/day/to/day/to/the/last/syllable/of/recorded/time/and/all/our/yesterdays/have/lighted/fools/the/way/to/dusty/death/out/out/brief/candle/life/is/but/a/walking/shadow/a/poor/player/that/struts/and/frets/his/hour/upon/the/stage/and/is/heard/no/more/it/is/a/tale/told/by/an/idiot/full/of/sound/and/fury/signifying/nothing');
    $this->assertText('Long author feed item title');
    $this->assertText('Long author feed item description');
    $this->assertLinkByHref('http://example.com/long/author');
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
