# aggregator_sanitize_configuration()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.module`](_file.md), lines 755–777 · [local source](../../../../source/modules/aggregator/aggregator.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module#L755-L777)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_sanitize_configuration()
```

## Documentation

```text
Checks and sanitizes the aggregator configuration.

Goes through all fetchers, parsers and processors and checks whether they
are available. If one is missing, resets to standard configuration.

@return
  TRUE if this function resets the configuration; FALSE if not.
```

## Code

```php
function aggregator_sanitize_configuration() {
  $reset = FALSE;
  list($fetcher, $parser, $processors) = _aggregator_get_variables();
  if (!module_exists($fetcher)) {
    $reset = TRUE;
  }
  if (!module_exists($parser)) {
    $reset = TRUE;
  }
  foreach ($processors as $processor) {
    if (!module_exists($processor)) {
      $reset = TRUE;
      break;
    }
  }
  if ($reset) {
    variable_del('aggregator_fetcher');
    variable_del('aggregator_parser');
    variable_del('aggregator_processors');
    return TRUE;
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.module](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module) · Licensed GPL-2.0-or-later (see LICENSE)._
