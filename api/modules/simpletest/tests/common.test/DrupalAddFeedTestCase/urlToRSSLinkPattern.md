# DrupalAddFeedTestCase::urlToRSSLinkPattern()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 3256–3261 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L3256-L3261)
- **Class:** [DrupalAddFeedTestCase](../DrupalAddFeedTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function urlToRSSLinkPattern($url, $title = '')
```

## Documentation

```text
Create a pattern representing the RSS feed in the page.
```

## Code

```php
  function urlToRSSLinkPattern($url, $title = '') {
    // Escape any regular expression characters in the URL ('?' is the worst).
    $url = preg_replace('/([+?.*])/', '[$0]', $url);
    $generated_pattern = '%<link +rel="alternate" +type="application/rss.xml" +title="' . $title . '" +href="' . $url . '" */>%';
    return $generated_pattern;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
