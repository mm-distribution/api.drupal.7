# AggregatorTestCase::getInvalidOpml()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 248–257 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L248-L257)
- **Class:** [AggregatorTestCase](../AggregatorTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
function getInvalidOpml()
```

## Documentation

```text
Creates an invalid OPML file.

@return
  Path to invalid OPML file.
```

## Code

```php
  function getInvalidOpml() {
    $opml = <<<EOF
<opml>
  <invalid>
</opml>
EOF;

    $path = 'public://invalid-opml.xml';
    return file_unmanaged_save_data($opml, $path);
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
