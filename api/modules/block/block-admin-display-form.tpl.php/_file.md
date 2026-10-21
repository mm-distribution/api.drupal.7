# modules/block/block-admin-display-form.tpl.php

- **Source:** [local](../../../../source/modules/block/block-admin-display-form.tpl.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block-admin-display-form.tpl.php) · 70 lines
- **Module/theme:** block

## File documentation

```text
@file
Default theme implementation to configure blocks.

Available variables:
- $block_regions: An array of regions. Keyed by name with the title as value.
- $block_listing: An array of blocks keyed by region and then delta.
- $form_submit: Form submit button.

Each $block_listing[$region] contains an array of blocks for that region.

Each $data in $block_listing[$region] contains:
- $data->region_title: Region title for the listed block.
- $data->block_title: Block title.
- $data->region_select: Drop-down menu for assigning a region.
- $data->weight_select: Drop-down menu for setting weights.
- $data->configure_link: Block configuration link.
- $data->delete_link: For deleting user added blocks.

@see template_preprocess_block_admin_display_form()
@see theme_block_admin_display()

@ingroup themeable
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
