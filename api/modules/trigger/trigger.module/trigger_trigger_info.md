# trigger_trigger_info()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 102–175 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L102-L175)
- **Module/theme:** trigger
- **Implements:** [hook_trigger_info()](../trigger.api.php/hook_trigger_info.md)

## Signature

```php
function trigger_trigger_info()
```

## Documentation

```text
Implements hook_trigger_info().

Defines all the triggers that this module implements triggers for.
```

## Code

```php
function trigger_trigger_info() {
   return array(
     'node' => array(
       'node_presave' => array(
         'label' => t('When either saving new content or updating existing content'),
       ),
       'node_insert' => array(
         'label' => t('After saving new content'),
       ),
       'node_update' => array(
         'label' => t('After saving updated content'),
       ),
       'node_delete' => array(
         'label' => t('After deleting content'),
       ),
       'node_view' => array(
         'label' => t('When content is viewed by an authenticated user'),
       ),
     ),
     'comment' => array(
       'comment_presave' => array(
         'label' => t('When either saving a new comment or updating an existing comment'),
       ),
       'comment_insert' => array(
         'label' => t('After saving a new comment'),
       ),
       'comment_update' => array(
         'label' => t('After saving an updated comment'),
       ),
       'comment_delete' => array(
         'label' => t('After deleting a comment'),
       ),
       'comment_view' => array(
         'label' => t('When a comment is being viewed by an authenticated user'),
       ),
     ),
     'taxonomy' => array(
       'taxonomy_term_insert' => array(
         'label' => t('After saving a new term to the database'),
       ),
       'taxonomy_term_update' => array(
         'label' => t('After saving an updated term to the database'),
       ),
       'taxonomy_term_delete' => array(
         'label' => t('After deleting a term'),
       ),
     ),
     'system' => array(
       'cron' => array(
         'label' => t('When cron runs'),
       ),
     ),
     'user' => array(
       'user_insert' => array(
         'label' => t('After creating a new user account'),
       ),
       'user_update' => array(
         'label' => t('After updating a user account'),
       ),
       'user_delete' => array(
         'label' => t('After a user has been deleted'),
       ),
       'user_login' => array(
         'label' => t('After a user has logged in'),
       ),
       'user_logout' => array(
         'label' => t('After a user has logged out'),
       ),
       'user_view' => array(
         'label' => t("When a user's profile is being viewed"),
       ),
     ),
   );
 }
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
