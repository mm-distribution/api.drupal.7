# DrupalTagsHandlingTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/common.test`](_file.md), lines 691–743 · [local source](../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L691-L743)
- **Module/theme:** batch_test

## Signature

```php
class DrupalTagsHandlingTestCase extends DrupalUnitTestCase
```

## Documentation

```text
Test drupal_explode_tags() and drupal_implode_tags().
```

## Properties

### $validTags

```php
var $validTags = array(
    'Drupal' => 'Drupal',
    'Drupal with some spaces' => 'Drupal with some spaces',
    '"Legendary Drupal mascot of doom: ""Druplicon"""' => 'Legendary Drupal mascot of doom: "Druplicon"',
    '"Drupal, although it rhymes with sloopal, is as awesome as a troopal!"' => 'Drupal, although it rhymes with sloopal, is as awesome as a troopal!',
  );
```

## Methods (derived index)

- [getInfo()](DrupalTagsHandlingTestCase/getInfo.md)
- [testDrupalExplodeTags()](DrupalTagsHandlingTestCase/testDrupalExplodeTags.md) — Explode a series of tags.
- [testDrupalImplodeTags()](DrupalTagsHandlingTestCase/testDrupalImplodeTags.md) — Implode a series of tags.
- [assertTags()](DrupalTagsHandlingTestCase/assertTags.md) — Helper function: asserts that the ending array of tags is what we wanted.

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
