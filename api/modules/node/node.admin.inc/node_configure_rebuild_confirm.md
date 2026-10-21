# node_configure_rebuild_confirm()

- **Type:** Function
- **File:** [`modules/node/node.admin.inc`](_file.md), lines 15–18 · [local source](../../../../source/modules/node/node.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.admin.inc#L15-L18)
- **Module/theme:** node
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function node_configure_rebuild_confirm()
```

## Documentation

```text
Menu callback: confirm rebuilding of permissions.

@see node_configure_rebuild_confirm_submit()
@see node_menu()
@ingroup forms
```

## Code

```php
function node_configure_rebuild_confirm() {
  return confirm_form(array(), t('Are you sure you want to rebuild the permissions on site content?'),
                  'admin/reports/status', t('This action rebuilds all permissions on site content, and may be a lengthy process. This action cannot be undone.'), t('Rebuild permissions'), t('Cancel'));
}
```

---
_Drupal 7.103 · [modules/node/node.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/node.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
