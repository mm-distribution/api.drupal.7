# hook_aggregator_parse_info()

- **Type:** Hook (documentation function)
- **File:** [`modules/aggregator/aggregator.api.php`](_file.md), lines 136–141 · [local source](../../../../source/modules/aggregator/aggregator.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.api.php#L136-L141)
- **Module/theme:** aggregator
- **Topics:** [hooks](../../../topics/hooks.md), aggregator

## Signature

```php
function hook_aggregator_parse_info()
```

## Documentation

```text
Specify the title and short description of your parser.

The title and the description provided are shown within the configuration
page. Use as title the human readable name of the parser and as description
a brief (40 to 80 characters) explanation of the parser's functionality.

This hook is only called if your module implements hook_aggregator_parse().
If this hook is not implemented aggregator will use your module's file name
as title and there will be no description.

@return
  An associative array defining a title and a description string.

@see hook_aggregator_parse()

@ingroup aggregator
```

## Code

```php
function hook_aggregator_parse_info() {
  return array(
    'title' => t('Default parser'),
    'description' => t('Default parser for RSS, Atom and RDF feeds.'),
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_aggregator_parse_info()".

- [aggregator_aggregator_parse_info()](../aggregator.parser.inc/aggregator_aggregator_parse_info.md) — `modules/aggregator/aggregator.parser.inc`

---
_Drupal 7.103 · [modules/aggregator/aggregator.api.php](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
