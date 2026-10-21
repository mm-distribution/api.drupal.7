# modules/user/user-picture.tpl.php

- **Source:** [local](../../../../source/modules/user/user-picture.tpl.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user-picture.tpl.php) · 24 lines
- **Module/theme:** user

## File documentation

```text
@file
Default theme implementation to present a picture configured for the
user's account.

Available variables:
- $user_picture: Image set by the user or the site's default. Will be linked
  depending on the viewer's permission to view the user's profile page.
- $account: Array of account information. Potentially unsafe. Be sure to
  check_plain() before use.

@see template_preprocess_user_picture()

@ingroup themeable
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
