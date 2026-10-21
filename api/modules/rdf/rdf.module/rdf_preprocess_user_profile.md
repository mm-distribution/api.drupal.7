# rdf_preprocess_user_profile()

- **Type:** Function
- **File:** [`modules/rdf/rdf.module`](_file.md), lines 571–603 · [local source](../../../../source/modules/rdf/rdf.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module#L571-L603)
- **Module/theme:** rdf

## Signature

```php
function rdf_preprocess_user_profile(&$variables)
```

## Documentation

```text
Implements MODULE_preprocess_HOOK().
```

## Code

```php
function rdf_preprocess_user_profile(&$variables) {
  $account = $variables['elements']['#account'];
  $uri = entity_uri('user', $account);

  // Adds RDFa markup to the user profile page. Fields displayed in this page
  // will automatically describe the user.
  if (!empty($account->rdf_mapping['rdftype'])) {
    $variables['attributes_array']['typeof'] = $account->rdf_mapping['rdftype'];
    $variables['attributes_array']['about'] = url($uri['path'], $uri['options']);
  }
  // Adds the relationship between the sioc:UserAccount and the foaf:Person who
  // holds the account.
  $account_holder_meta = array(
    '#tag' => 'meta',
    '#attributes' => array(
      'about' => url($uri['path'], array_merge($uri['options'], array('fragment' => 'me'))),
      'typeof' => array('foaf:Person'),
      'rel' => array('foaf:account'),
      'resource' => url($uri['path'], $uri['options']),
    ),
  );
  // Adds the markup for username.
  $username_meta = array(
    '#tag' => 'meta',
    '#attributes' => array(
      'about' => url($uri['path'], $uri['options']),
      'property' => $account->rdf_mapping['name']['predicates'],
      'content' => $account->name,
    )
  );
  drupal_add_html_head($account_holder_meta, 'rdf_user_account_holder');
  drupal_add_html_head($username_meta, 'rdf_user_username');
}
```

---
_Drupal 7.103 · [modules/rdf/rdf.module](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module) · Licensed GPL-2.0-or-later (see LICENSE)._
