# openid_begin()

- **Type:** Function
- **File:** [`modules/openid/openid.module`](_file.md), lines 261–317 · [local source](../../../../source/modules/openid/openid.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module#L261-L317)
- **Module/theme:** openid

## Signature

```php
function openid_begin($claimed_id, $return_to = '', $form_values = array())
```

## Documentation

```text
The initial step of OpenID authentication responsible for the following:
 - Perform discovery on the claimed OpenID.
 - If possible, create an association with the Provider's endpoint.
 - Create the authentication request.
 - Perform the appropriate redirect.

@param $claimed_id The OpenID to authenticate
@param $return_to The endpoint to return to from the OpenID Provider
```

## Code

```php
function openid_begin($claimed_id, $return_to = '', $form_values = array()) {
  module_load_include('inc', 'openid');

  $service = NULL;
  $claimed_id = openid_normalize($claimed_id);
  $discovery = openid_discovery($claimed_id);

  if (!empty($discovery['services'])) {
    $service = _openid_select_service($discovery['services']);
  }

  // Quit if the discovery result was empty or if we can't select any service.
  if (!$discovery || !$service) {
    form_set_error('openid_identifier', t('Sorry, that is not a valid OpenID. Ensure you have spelled your ID correctly.'));
    return;
  }

  // Set claimed id from discovery.
  if (!empty($discovery['claimed_id'])) {
    $claimed_id = $discovery['claimed_id'];
  }

  // Store discovered information in the users' session so we don't have to rediscover.
  $_SESSION['openid']['service'] = $service;
  // Store the claimed id
  $_SESSION['openid']['claimed_id'] = $claimed_id;
  // Store the login form values so we can pass them to
  // user_exteral_login later.
  $_SESSION['openid']['user_login_values'] = $form_values;

  // If a supported math library is present, then create an association.
  $assoc_handle = '';
  if (_openid_get_math_library()) {
    $assoc_handle = openid_association($service['uri']);
  }

  if (in_array('http://specs.openid.net/auth/2.0/server', $service['types'])) {
    // User entered an OP Identifier.
    $claimed_id = $identity = 'http://specs.openid.net/auth/2.0/identifier_select';
  }
  else {
    // Use Claimed ID and/or OP-Local Identifier from service description, if
    // available.
    if (!empty($service['claimed_id'])) {
      $claimed_id = $service['claimed_id'];
    }
    $identity = !empty($service['identity']) ? $service['identity'] : $claimed_id;
  }
  $request = openid_authentication_request($claimed_id, $identity, $return_to, $assoc_handle, $service);

  if ($service['version'] == 2) {
    openid_redirect($service['uri'], $request);
  }
  else {
    openid_redirect_http($service['uri'], $request);
  }
}
```

---
_Drupal 7.103 · [modules/openid/openid.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module) · Licensed GPL-2.0-or-later (see LICENSE)._
