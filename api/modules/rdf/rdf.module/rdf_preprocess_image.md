# rdf_preprocess_image()

- **Type:** Function
- **File:** [`modules/rdf/rdf.module`](_file.md), lines 770–775 · [local source](../../../../source/modules/rdf/rdf.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module#L770-L775)
- **Module/theme:** rdf

## Signature

```php
function rdf_preprocess_image(&$variables)
```

## Documentation

```text
Implements MODULE_preprocess_HOOK().
```

## Code

```php
function rdf_preprocess_image(&$variables) {
  // Adds the RDF type for image. We cannot use the usual entity-based mapping
  // to get 'foaf:Image' because image does not have its own entity type or
  // bundle.
  $variables['attributes']['typeof'] = array('foaf:Image');
}
```

---
_Drupal 7.103 · [modules/rdf/rdf.module](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module) · Licensed GPL-2.0-or-later (see LICENSE)._
