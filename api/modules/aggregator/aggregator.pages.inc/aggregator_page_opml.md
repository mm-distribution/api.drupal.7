# aggregator_page_opml()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.pages.inc`](_file.md), lines 479–489 · [local source](../../../../source/modules/aggregator/aggregator.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc#L479-L489)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_page_opml($cid = NULL)
```

## Documentation

```text
Page callback: Generates an OPML representation of all feeds.

@param $cid
  (optional) If set, feeds are exported only from a category with this ID.
  Otherwise, all feeds are exported. Defaults to NULL.

@return
  An OPML formatted string.
```

## Code

```php
function aggregator_page_opml($cid = NULL) {
  if ($cid) {
    $result = db_query('SELECT f.title, f.url FROM {aggregator_feed} f LEFT JOIN {aggregator_category_feed} c on f.fid = c.fid WHERE c.cid = :cid ORDER BY title', array(':cid' => $cid));
  }
  else {
    $result = db_query('SELECT * FROM {aggregator_feed} ORDER BY title');
  }

  $feeds = $result->fetchAll();
  return theme('aggregator_page_opml', array('feeds' => $feeds));
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
