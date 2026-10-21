# openid_authentication_request()

- **Type:** Function
- **File:** [`modules/openid/openid.module`](_file.md), lines 746–811 · [local source](../../../../source/modules/openid/openid.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module#L746-L811)
- **Module/theme:** openid

## Signature

```php
function openid_authentication_request($claimed_id, $identity, $return_to, $assoc_handle, $service)
```

## Documentation

_No docblock in source._

## Code

```php
function openid_authentication_request($claimed_id, $identity, $return_to, $assoc_handle, $service) {
  global $base_url;

  module_load_include('inc', 'openid');

  $request =  array(
    'openid.mode' => 'checkid_setup',
    'openid.identity' => $identity,
    'openid.assoc_handle' => $assoc_handle,
    'openid.return_to' => $return_to,
  );

  if ($service['version'] == 2) {
    $request['openid.ns'] = OPENID_NS_2_0;
    $request['openid.claimed_id'] = $claimed_id;
    $request['openid.realm'] = $base_url .'/';
  }
  else {
    $request['openid.trust_root'] = $base_url .'/';
  }

  // Always request Simple Registration. The specification doesn't mandate
  // that the Endpoint advertise OPENID_NS_SREG in the service description.
  $request['openid.ns.sreg'] = OPENID_NS_SREG;
  $request['openid.sreg.required'] = 'nickname,email';

  // Request Attribute Exchange, if available.
  // We only request the minimum attributes we need here, contributed modules
  // can alter the request to add more attribute, and map them to profile fields.
  if (in_array(OPENID_NS_AX, $service['types'])) {
    $request['openid.ns.ax'] = OPENID_NS_AX;
    $request['openid.ax.mode'] = 'fetch_request';
    $request['openid.ax.required'] = 'mail_ao,name_ao,mail_son,name_son';

    // Implementors disagree on which URIs to use, even for simple
    // attributes like name and email (*sigh*). We ask for both axschema.org
    // attributes (which are supposed to be newer), and schema.openid.net ones
    // (which are supposed to be legacy).

    // Attributes as defined by axschema.org.
    $request['openid.ax.type.mail_ao'] = 'http://axschema.org/contact/email';
    $request['openid.ax.type.name_ao'] = 'http://axschema.org/namePerson/friendly';

    // Attributes as defined by schema.openid.net.
    $request['openid.ax.type.mail_son'] = 'http://schema.openid.net/contact/email';
    $request['openid.ax.type.name_son'] = 'http://schema.openid.net/namePerson/friendly';
  }

  $request = array_merge($request, module_invoke_all('openid', 'request', $request));

  // module_invoke_all() uses array_merge_recursive() which might return nested
  // arrays if two or more modules alter a given parameter, resulting in an
  // invalid request format. To ensure this doesn't happen, we flatten the returned
  // value by taking the last entry in the array if an array is returned.
  $flattened_request = array();
  foreach ($request as $key => $value) {
    if (is_array($value)) {
      $flattened_request[$key] = end($value);
    }
    else {
      $flattened_request[$key] = $value;
    }
  }

  return $flattened_request;
}
```

---
_Drupal 7.103 · [modules/openid/openid.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module) · Licensed GPL-2.0-or-later (see LICENSE)._
