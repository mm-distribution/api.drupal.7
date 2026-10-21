# _simpletest_format_summary_line()

- **Type:** Function
- **File:** [`modules/simpletest/simpletest.module`](_file.md), lines 103–114 · [local source](../../../../source/modules/simpletest/simpletest.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module#L103-L114)
- **Module/theme:** simpletest

## Signature

```php
function _simpletest_format_summary_line($summary)
```

## Documentation

_No docblock in source._

## Code

```php
function _simpletest_format_summary_line($summary) {
  $args = array(
    '@pass' => format_plural(isset($summary['#pass']) ? $summary['#pass'] : 0, '1 pass', '@count passes'),
    '@fail' => format_plural(isset($summary['#fail']) ? $summary['#fail'] : 0, '1 fail', '@count fails'),
    '@exception' => format_plural(isset($summary['#exception']) ? $summary['#exception'] : 0, '1 exception', '@count exceptions'),
  );
  if (!$summary['#debug']) {
    return t('@pass, @fail, and @exception', $args);
  }
  $args['@debug'] = format_plural(isset($summary['#debug']) ? $summary['#debug'] : 0, '1 debug message', '@count debug messages');
  return t('@pass, @fail, @exception, and @debug', $args);
}
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module) · Licensed GPL-2.0-or-later (see LICENSE)._
