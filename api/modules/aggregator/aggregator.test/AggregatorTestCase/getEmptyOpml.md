# AggregatorTestCase::getEmptyOpml()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 265–279 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L265-L279)
- **Class:** [AggregatorTestCase](../AggregatorTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
function getEmptyOpml()
```

## Documentation

```text
Creates a valid but empty OPML file.

@return
  Path to empty OPML file.
```

## Code

```php
  function getEmptyOpml() {
    $opml = <<<EOF
<?xml version="1.0" encoding="utf-8"?>
<opml version="1.0">
  <head></head>
  <body>
    <outline text="Sample text" />
    <outline text="Sample text" url="Sample URL" />
  </body>
</opml>
EOF;

    $path = 'public://empty-opml.xml';
    return file_unmanaged_save_data($opml, $path);
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
