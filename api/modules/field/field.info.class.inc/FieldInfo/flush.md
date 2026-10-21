# FieldInfo::flush()

- **Type:** Method
- **File:** [`modules/field/field.info.class.inc`](../_file.md), lines 97–112 · [local source](../../../../../source/modules/field/field.info.class.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.class.inc#L97-L112)
- **Class:** [FieldInfo](../FieldInfo.md)
- **Module/theme:** field

## Signature

```php
public function flush()
```

## Documentation

```text
Clears the "static" and persistent caches.
```

## Code

```php
  public function flush() {
    $this->fieldMap = NULL;

    $this->fieldsById = array();
    $this->fieldIdsByName = array();
    $this->loadedAllFields = FALSE;
    $this->unknownFields = array();

    $this->bundleInstances = array();
    $this->loadedAllInstances = FALSE;
    $this->emptyBundles = array();

    $this->bundleExtraFields = array();

    cache_clear_all('field_info:', 'cache_field', TRUE);
  }
```

---
_Drupal 7.103 · [modules/field/field.info.class.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.class.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
