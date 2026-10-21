# UpgradePathTaxonomyTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.taxonomy.test`](../_file.md), lines 7–13 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.taxonomy.test#L7-L13)
- **Class:** [UpgradePathTaxonomyTestCase](../UpgradePathTaxonomyTestCase.md)
- **Module/theme:** batch_test

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
      'name'  => 'Taxonomy upgrade path',
      'description'  => 'Taxonomy upgrade path tests.',
      'group' => 'Upgrade path',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
