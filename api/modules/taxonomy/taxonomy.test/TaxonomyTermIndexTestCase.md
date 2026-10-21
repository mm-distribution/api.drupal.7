# TaxonomyTermIndexTestCase

- **Type:** Class
- **File:** [`modules/taxonomy/taxonomy.test`](_file.md), lines 1174–1395 · [local source](../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L1174-L1395)
- **Module/theme:** taxonomy

## Signature

```php
class TaxonomyTermIndexTestCase extends TaxonomyWebTestCase
```

## Documentation

```text
Tests the hook implementations that maintain the taxonomy index.
```

## Properties

### $vocabulary

```php
protected $vocabulary;
```

### $instance_1

```php
protected $instance_1;
```

### $field_name_1

```php
protected $field_name_1;
```

### $field_1

```php
protected $field_1;
```

### $instance_2

```php
protected $instance_2;
```

### $field_name_2

```php
protected $field_name_2;
```

### $field_2

```php
protected $field_2;
```

### $admin_user

```php
protected $admin_user;
```

## Methods (derived index)

- [getInfo()](TaxonomyTermIndexTestCase/getInfo.md)
- [setUp()](TaxonomyTermIndexTestCase/setUp.md)
- [testTaxonomyIndex()](TaxonomyTermIndexTestCase/testTaxonomyIndex.md) — Tests that the taxonomy index is maintained properly.
- [testTaxonomyTermHierarchyBreadcrumbs()](TaxonomyTermIndexTestCase/testTaxonomyTermHierarchyBreadcrumbs.md) — Tests that there is a link to the parent term on the child term page.

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
