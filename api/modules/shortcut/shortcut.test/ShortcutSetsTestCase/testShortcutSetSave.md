# ShortcutSetsTestCase::testShortcutSetSave()

- **Type:** Method
- **File:** [`modules/shortcut/shortcut.test`](../_file.md), lines 304–314 · [local source](../../../../../source/modules/shortcut/shortcut.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test#L304-L314)
- **Class:** [ShortcutSetsTestCase](../ShortcutSetsTestCase.md)
- **Module/theme:** shortcut

## Signature

```php
function testShortcutSetSave()
```

## Documentation

```text
Tests that shortcut_set_save() correctly updates existing links.
```

## Code

```php
  function testShortcutSetSave() {
    $set = $this->set;
    $old_mlids = $this->getShortcutInformation($set, 'mlid');

    $set->links[] = $this->generateShortcutLink('admin', $this->randomName(10));
    shortcut_set_save($set);
    $saved_set = shortcut_set_load($set->set_name);

    $new_mlids = $this->getShortcutInformation($saved_set, 'mlid');
    $this->assertTrue(count(array_intersect($old_mlids, $new_mlids)) == count($old_mlids), 'shortcut_set_save() did not inadvertently change existing mlids.');
  }
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.test](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test) · Licensed GPL-2.0-or-later (see LICENSE)._
