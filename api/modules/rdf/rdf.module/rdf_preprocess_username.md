# rdf_preprocess_username()

- **Type:** Function
- **File:** [`modules/rdf/rdf.module`](_file.md), lines 608–660 · [local source](../../../../source/modules/rdf/rdf.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module#L608-L660)
- **Module/theme:** rdf

## Signature

```php
function rdf_preprocess_username(&$variables)
```

## Documentation

```text
Implements MODULE_preprocess_HOOK().
```

## Code

```php
function rdf_preprocess_username(&$variables) {
  // Because xml:lang is set on the HTML element that wraps the page, the
  // username inherits this language attribute. However, since the username
  // might not be transliterated to the same language that the content is in,
  // we do not want it to inherit the language attribute, so we set the
  // attribute to an empty string.
  if (empty($variables['attributes_array']['xml:lang'])) {
    $variables['attributes_array']['xml:lang'] = '';
  }

  // $variables['account'] is a pseudo account object, and as such, does not
  // contain the RDF mappings for the user. In the case of nodes and comments,
  // it contains the mappings for the node or comment object instead. However,
  // while the RDF mappings are available from a full user_load(), this should
  // be avoided for performance reasons. Since the type and bundle for users is
  // already known, call rdf_mapping_load() directly.
  $rdf_mapping = rdf_mapping_load('user', 'user');

  // The profile URI is used to identify the user account. The about attribute
  // is used to set the URI as the default subject of the predicates embedded
  // as RDFa in the child elements. Even if the user profile is not accessible
  // to the current user, we use its URI in order to identify the user in RDF.
  // We do not use this attribute for the anonymous user because we do not have
  // a user profile URI for it (only a homepage which cannot be used as user
  // profile in RDF.)
  if ($variables['uid'] > 0) {
    $variables['attributes_array']['about'] = url('user/' . $variables['uid']);
  }

  $attributes = array();
  // The typeof attribute specifies the RDF type(s) of this resource. They
  // are defined in the 'rdftype' property of the user RDF mapping.
  if (!empty($rdf_mapping['rdftype'])) {
    $attributes['typeof'] = $rdf_mapping['rdftype'];
  }
  // Annotate the username in RDFa. A property attribute is used with an empty
  // datatype attribute to ensure the username is parsed as a plain literal
  // in RDFa 1.0 and 1.1.
  if (!empty($rdf_mapping['name'])) {
    $attributes['property'] = $rdf_mapping['name']['predicates'];
    $attributes['datatype'] = '';
  }
  // Add the homepage RDFa markup if present.
  if (!empty($variables['homepage']) && !empty($rdf_mapping['homepage'])) {
    $attributes['rel'] = $rdf_mapping['homepage']['predicates'];
  }
  // The remaining attributes can have multiple values listed, with whitespace
  // separating the values in the RDFa attributes
  // (see http://www.w3.org/TR/rdfa-syntax/#rdfa-attributes).
  // Therefore, merge rather than override so as not to clobber values set by
  // earlier preprocess functions.
  $variables['attributes_array'] = array_merge_recursive($variables['attributes_array'], $attributes);
}
```

---
_Drupal 7.103 · [modules/rdf/rdf.module](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module) · Licensed GPL-2.0-or-later (see LICENSE)._
