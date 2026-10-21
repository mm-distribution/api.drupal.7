# ImportOPMLTestCase::testOPMLImport()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 856–860 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L856-L860)
- **Class:** [ImportOPMLTestCase](../ImportOPMLTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
function testOPMLImport()
```

## Documentation

```text
Tests the import of an OPML file.
```

## Code

```php
  function testOPMLImport() {
    $this->openImportForm();
    $this->validateImportFormFields();
    $this->submitImportForm();
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
