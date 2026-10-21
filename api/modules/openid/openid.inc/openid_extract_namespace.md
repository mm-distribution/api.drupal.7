# openid_extract_namespace()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 648–680 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L648-L680)
- **Module/theme:** openid

## Signature

```php
function openid_extract_namespace($response, $extension_namespace, $fallback_prefix = NULL, $only_signed = FALSE)
```

## Documentation

```text
Extract all the parameters belonging to an extension in a response message.

OpenID 2.0 defines a simple extension mechanism, based on a namespace prefix.

Each request or response can define a prefix using:
@code
  openid.ns.[prefix] = [extension_namespace]
  openid.[prefix].[key1] = [value1]
  openid.[prefix].[key2] = [value2]
  ...
@endcode

This function extracts all the keys belonging to an extension namespace in a
response, optionally using a fallback prefix if none is provided in the response.

Note that you cannot assume that a given extension namespace will use the same
prefix on the response and the request: each party may use a different prefix
to refer to the same namespace.

@param $response
  The response array.
@param $extension_namespace
  The namespace of the extension.
@param $fallback_prefix
  An optional prefix that will be used in case no prefix is found for the
  target extension namespace.
@param $only_signed
  Return only keys that are included in the message signature in openid.sig.
  Unsigned fields may have been modified or added by other parties than the
  OpenID Provider.

@return
  An associative array containing all the parameters in the response message
  that belong to the extension. The keys are stripped from their namespace
  prefix.

@see http://openid.net/specs/openid-authentication-2_0.html#extensions
```

## Code

```php
function openid_extract_namespace($response, $extension_namespace, $fallback_prefix = NULL, $only_signed = FALSE) {
  $signed_keys = explode(',', $response['openid.signed']);

  // Find the namespace prefix.
  $prefix = $fallback_prefix;
  foreach ($response as $key => $value) {
    if ($value == $extension_namespace && preg_match('/^openid\.ns\.([^.]+)$/', $key, $matches)) {
      $prefix = $matches[1];
      if ($only_signed && !in_array('ns.' . $matches[1], $signed_keys)) {
        // The namespace was defined but was not signed as required. In this
        // case we do not fall back to $fallback_prefix.
        $prefix = NULL;
      }
      break;
    }
  }

  // Now extract the namespace keys from the response.
  $output = array();
  if (!isset($prefix)) {
    return $output;
  }
  foreach ($response as $key => $value) {
    if (preg_match('/^openid\.' . $prefix . '\.(.+)$/', $key, $matches)) {
      $local_key = $matches[1];
      if (!$only_signed || in_array($prefix . '.' . $local_key, $signed_keys)) {
        $output[$local_key] = $value;
      }
    }
  }

  return $output;
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
