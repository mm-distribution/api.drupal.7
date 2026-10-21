# FilterUnitTestCase::filterUrlWithPcreErrors()

- **Type:** Method
- **File:** [`modules/filter/filter.test`](../_file.md), lines 1917–1925 · [local source](../../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L1917-L1925)
- **Class:** [FilterUnitTestCase](../FilterUnitTestCase.md)
- **Module/theme:** filter

## Signature

```php
protected function filterUrlWithPcreErrors($input, $filter)
```

## Documentation

```text
Calls filter_url with pcre.backtrack_limit set to 1.

When PCRE errors occur, _filter_url() returns the input text unchanged.

@param $input
  Text to pass on to _filter_url().
@param $filter
  Filter to pass on to _filter_url().
@return
  The processed $input.
```

## Code

```php
  protected function filterUrlWithPcreErrors($input, $filter) {
    $pcre_backtrack_limit = ini_get('pcre.backtrack_limit');
    // Setting this limit to the smallest possible value should cause PCRE
    // errors and break the various preg_* functions used by _filter_url().
    ini_set('pcre.backtrack_limit', 1);
    $result = _filter_url($input, $filter);
    ini_set('pcre.backtrack_limit', $pcre_backtrack_limit);
    return $result;
  }
```

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
