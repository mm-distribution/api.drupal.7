# AggregatorTestCase::getFeedEditArray()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 63–77 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L63-L77)
- **Class:** [AggregatorTestCase](../AggregatorTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
function getFeedEditArray($feed_url = NULL)
```

## Documentation

```text
Returns a randomly generated feed edit array.

@param $feed_url
  (optional) If given, feed will be created with this URL, otherwise
  /rss.xml will be used. Defaults to NULL.
@return
  A feed array.
```

## Code

```php
  function getFeedEditArray($feed_url = NULL) {
    $feed_name = $this->randomName(10);
    if (!$feed_url) {
      $feed_url = url('rss.xml', array(
        'query' => array('feed' => $feed_name),
        'absolute' => TRUE,
      ));
    }
    $edit = array(
      'title' => $feed_name,
      'url' => $feed_url,
      'refresh' => '900',
    );
    return $edit;
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
