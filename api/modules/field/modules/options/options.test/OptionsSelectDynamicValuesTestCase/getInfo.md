# OptionsSelectDynamicValuesTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/field/modules/options/options.test`](../_file.md), lines 550–556 · [local source](../../../../../../../source/modules/field/modules/options/options.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.test#L550-L556)
- **Class:** [OptionsSelectDynamicValuesTestCase](../OptionsSelectDynamicValuesTestCase.md)
- **Module/theme:** options

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'Options select dynamic values',
      'description' => 'Test an options select on a list field with a dynamic allowed values function.',
      'group' => 'Field types',
    );
  }
```

---
_Drupal 7.103 · [modules/field/modules/options/options.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.test) · Licensed GPL-2.0-or-later (see LICENSE)._
