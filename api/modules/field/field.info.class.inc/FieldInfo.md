# FieldInfo

- **Type:** Class
- **File:** [`modules/field/field.info.class.inc`](_file.md), lines 29–686 · [local source](../../../../source/modules/field/field.info.class.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.class.inc#L29-L686)
- **Module/theme:** field

## Signature

```php
class FieldInfo
```

## Documentation

```text
Provides field and instance definitions for the current runtime environment.

A FieldInfo object is created and statically persisted through the request
by the _field_info_field_cache() function. The object properties act as a
"static cache" of fields and instances definitions.

The preferred way to access definitions is through the getBundleInstances()
method, which keeps cache entries per bundle, storing both fields and
instances for a given bundle. Fields used in multiple bundles are duplicated
in several cache entries, and are merged into a single list in the memory
cache. Cache entries are loaded for bundles as a whole, optimizing memory
and CPU usage for the most common pattern of iterating over all instances of
a bundle rather than accessing a single instance.

The getFields() and getInstances() methods, which return all existing field
and instance definitions, are kept mainly for backwards compatibility, and
should be avoided when possible, since they load and persist in memory a
potentially large array of information. In many cases, the lightweight
getFieldMap() method should be preferred.
```

## Properties

### $fieldMap

```php
protected $fieldMap;
```

```text
Lightweight map of fields across entity types and bundles.

@var array
```

### $fieldsById

```php
protected $fieldsById = array();
```

```text
List of $field structures keyed by ID. Includes deleted fields.

@var array
```

### $fieldIdsByName

```php
protected $fieldIdsByName = array();
```

```text
Mapping of field names to the ID of the corresponding non-deleted field.

@var array
```

### $loadedAllFields

```php
protected $loadedAllFields = FALSE;
```

```text
Whether $fieldsById contains all field definitions or a subset.

@var bool
```

### $unknownFields

```php
protected $unknownFields = array();
```

```text
Separately tracks requested field names or IDs that do not exist.

@var array
```

### $bundleInstances

```php
protected $bundleInstances = array();
```

```text
Instance definitions by bundle.

@var array
```

### $loadedAllInstances

```php
protected $loadedAllInstances = FALSE;
```

```text
Whether $bundleInstances contains all instances definitions or a subset.

@var bool
```

### $emptyBundles

```php
protected $emptyBundles = array();
```

```text
Separately tracks requested bundles that are empty (or do not exist).

@var array
```

### $bundleExtraFields

```php
protected $bundleExtraFields = array();
```

```text
Extra fields by bundle.

@var array
```

## Methods (derived index)

- [flush()](FieldInfo/flush.md) — Clears the "static" and persistent caches.
- [getFieldMap()](FieldInfo/getFieldMap.md) — Collects a lightweight map of fields across bundles.
- [getFields()](FieldInfo/getFields.md) — Returns all active fields, including deleted ones.
- [getInstances()](FieldInfo/getInstances.md) — Retrieves all active, non-deleted instances definitions.
- [getField()](FieldInfo/getField.md) — Returns a field definition from a field name.
- [getFieldById()](FieldInfo/getFieldById.md) — Returns a field definition from a field ID.
- [getBundleInstances()](FieldInfo/getBundleInstances.md) — Retrieves the instances for a bundle.
- [getBundleExtraFields()](FieldInfo/getBundleExtraFields.md) — Retrieves the "extra fields" for a bundle.
- [prepareField()](FieldInfo/prepareField.md) — Prepares a field definition for the current run-time context.
- [prepareInstance()](FieldInfo/prepareInstance.md) — Prepares an instance definition for the current run-time context.
- [prepareInstanceWidget()](FieldInfo/prepareInstanceWidget.md) — Prepares widget properties for the current run-time context.
- [prepareInstanceDisplay()](FieldInfo/prepareInstanceDisplay.md) — Adapts display specifications to the current run-time context.
- [prepareExtraFields()](FieldInfo/prepareExtraFields.md) — Prepares 'extra fields' for the current run-time context.

---
_Drupal 7.103 · [modules/field/field.info.class.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.class.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
