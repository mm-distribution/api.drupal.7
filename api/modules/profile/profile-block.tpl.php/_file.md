# modules/profile/profile-block.tpl.php

- **Source:** [local](../../../../source/modules/profile/profile-block.tpl.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile-block.tpl.php) · 42 lines
- **Module/theme:** profile

## File documentation

```text
@file
Default theme implementation for displaying a users profile within a
block. It only shows in relation to a node displayed as a full page.

Available variables:
- $user_picture: Image configured for the account linking to the users page.
- $profile: Keyed array of all profile fields that have a value.

Each $field in $profile contains:
- $field->title: Title of the profile field.
- $field->value: Value of the profile field.
- $field->type: Type of the profile field, i.e., checkbox, textfield,
  textarea, selection, list, url or date.

Since $profile is keyed, a direct print of the field is possible. Not
all accounts may have a value for a profile so do a check first. If a field
of "last_name" was set for the site, the following can be used.

 <?php if (isset($profile['last_name'])): ?>
   <div class="field last-name">
     <?php print $profile['last_name']->title; ?>:<br />
     <?php print $profile['last_name']->value; ?>
   </div>
 <?php endif; ?>

@see template_preprocess_profile_block()
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
