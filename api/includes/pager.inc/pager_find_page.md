# pager_find_page()

- **Type:** Function
- **File:** [`includes/pager.inc`](_file.md), lines 202–209 · [local source](../../../source/includes/pager.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/pager.inc#L202-L209)

## Signature

```php
function pager_find_page($element = 0)
```

## Documentation

```text
Returns the current page being requested for display within a pager.

@param $element
 An optional integer to distinguish between multiple pagers on one page.

@return
 The number of the current requested page, within the pager represented by
 $element. This is determined from the URL query parameter $_GET['page'], or
 0 by default. Note that this number may differ from the actual page being
 displayed. For example, if a search for "example text" brings up three
 pages of results, but a users visits search/node/example+text?page=10, this
 function will return 10, even though the default pager implementation
 adjusts for this and still displays the third page of search results at
 that URL.

@see pager_default_initialize()
```

## Code

```php
function pager_find_page($element = 0) {
  $page = isset($_GET['page']) ? $_GET['page'] : '';
  $page_array = explode(',', $page);
  if (!isset($page_array[$element])) {
    $page_array[$element] = 0;
  }
  return (int) $page_array[$element];
}
```

---
_Drupal 7.103 · [includes/pager.inc](https://github.com/drupal/drupal/blob/7.103/includes/pager.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
