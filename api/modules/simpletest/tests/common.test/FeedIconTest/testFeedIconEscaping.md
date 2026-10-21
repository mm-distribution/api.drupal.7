# FeedIconTest::testFeedIconEscaping()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 3280–3287 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L3280-L3287)
- **Class:** [FeedIconTest](../FeedIconTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testFeedIconEscaping()
```

## Documentation

```text
Check that special characters are correctly escaped. Test for issue #1211668.
```

## Code

```php
  function testFeedIconEscaping() {
    $variables = array();
    $variables['url'] = 'node';
    $variables['title'] = '<>&"\'';
    $text = theme_feed_icon($variables);
    preg_match('/title="(.*?)"/', $text, $matches);
    $this->assertEqual($matches[1], 'Subscribe to &amp;&quot;&#039;', 'theme_feed_icon() escapes reserved HTML characters.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
