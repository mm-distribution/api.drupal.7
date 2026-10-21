# user_rdf_mapping()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 4121–4138 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L4121-L4138)
- **Module/theme:** user
- **Implements:** [hook_rdf_mapping()](../../rdf/rdf.api.php/hook_rdf_mapping.md)

## Signature

```php
function user_rdf_mapping()
```

## Documentation

```text
Implements hook_rdf_mapping().
```

## Code

```php
function user_rdf_mapping() {
  return array(
    array(
      'type' => 'user',
      'bundle' => RDF_DEFAULT_BUNDLE,
      'mapping' => array(
        'rdftype' => array('sioc:UserAccount'),
        'name' => array(
          'predicates' => array('foaf:name'),
        ),
        'homepage' => array(
          'predicates' => array('foaf:page'),
          'type' => 'rel',
        ),
      ),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
