# modules/openid/openid.module

- **Source:** [local](../../../../source/modules/openid/openid.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module) · 1041 lines
- **Module/theme:** openid

## File documentation

```text
@file
Implement OpenID Relying Party support for Drupal
```

## Functions (derived index)

- [openid_menu()](openid_menu.md) — Implements hook_menu().
- [openid_menu_site_status_alter()](openid_menu_site_status_alter.md) — Implements hook_menu_site_status_alter().
- [openid_admin_paths()](openid_admin_paths.md) — Implements hook_admin_paths().
- [openid_help()](openid_help.md) — Implements hook_help().
- [openid_user_insert()](openid_user_insert.md) — Implements hook_user_insert().
- [openid_user_login()](openid_user_login.md) — Implements hook_user_login().
- [openid_user_logout()](openid_user_logout.md) — Implements hook_user_logout().
- [openid_form_user_login_block_alter()](openid_form_user_login_block_alter.md) — Implements hook_form_FORM_ID_alter().
- [openid_form_user_login_alter()](openid_form_user_login_alter.md) — Implements hook_form_FORM_ID_alter().
- [_openid_user_login_form_alter()](_openid_user_login_form_alter.md)
- [openid_form_user_register_form_alter()](openid_form_user_register_form_alter.md) — Implements hook_form_FORM_ID_alter().
- [openid_login_validate()](openid_login_validate.md) — Login form _validate hook
- [openid_begin()](openid_begin.md) — The initial step of OpenID authentication responsible for the following: - Perform discovery on the claimed OpenID. - If possible, create an association with the Provider's endpoint. - Create the authentication request. - Perform the appropriate redirect.
- [openid_complete()](openid_complete.md) — Completes OpenID authentication by validating returned data from the OpenID Provider.
- [openid_discovery()](openid_discovery.md) — Perform discovery on a claimed ID to determine the OpenID provider endpoint.
- [openid_openid_discovery_method_info()](openid_openid_discovery_method_info.md) — Implements hook_openid_discovery_method_info().
- [_openid_xri_discovery()](_openid_xri_discovery.md) — OpenID discovery method: perform an XRI discovery.
- [_openid_xrds_discovery()](_openid_xrds_discovery.md) — OpenID discovery method: perform a XRDS discovery.
- [openid_openid_normalization_method_info()](openid_openid_normalization_method_info.md) — Implements hook_openid_normalization_method_info().
- [openid_association()](openid_association.md) — Attempt to create a shared secret with the OpenID Provider.
- [openid_authentication()](openid_authentication.md) — Authenticate a user or attempt registration.
- [openid_association_request()](openid_association_request.md)
- [openid_authentication_request()](openid_authentication_request.md)
- [openid_verify_assertion()](openid_verify_assertion.md) — Attempt to verify the response received from the OpenID Provider.
- [openid_verify_assertion_signature()](openid_verify_assertion_signature.md) — Verify the signature of the response received from the OpenID provider.
- [openid_verify_assertion_nonce()](openid_verify_assertion_nonce.md) — Verify that the nonce has not been used in earlier assertions from the same OpenID provider.
- [openid_verify_assertion_return_url()](openid_verify_assertion_return_url.md) — Verify that openid.return_to matches the current URL.
- [openid_cron()](openid_cron.md) — Remove expired nonces from the database.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
