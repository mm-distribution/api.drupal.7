# Field API

- **Topic id:** `field`
- **Defined in:** [`modules/field/field.module`](../modules/field/field.module/_file.md), line 27 · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module#L27)

## Documentation

```text
@defgroup field Field API
@{
Attach custom data fields to Drupal entities.

The Field API allows custom data fields to be attached to Drupal
entities and takes care of storing, loading, editing, and rendering
field data. Any entity type (node, user, etc.) can use the Field
API to make itself "fieldable" and thus allow fields to be attached
to it. Other modules can provide a user interface for managing custom
fields via a web browser as well as a wide and flexible variety of
data type, form element, and display format capabilities.

The Field API defines two primary data structures, Field and
Instance, and the concept of a Bundle. A Field defines a
particular type of data that can be attached to entities. A Field
Instance is a Field attached to a single Bundle. A Bundle is a set
of fields that are treated as a group by the Field Attach API and
is related to a single fieldable entity type.

For example, suppose a site administrator wants Article nodes to
have a subtitle and photo. Using the Field API or Field UI module,
the administrator creates a field named 'subtitle' of type 'text'
and a field named 'photo' of type 'image'. The administrator
(again, via a UI) creates two Field Instances, one attaching the
field 'subtitle' to the 'node' bundle 'article' and one attaching
the field 'photo' to the 'node' bundle 'article'. When the node
system uses the Field Attach API to load all fields for an Article
node, it passes the node's entity type (which is 'node') and
content type (which is 'article') as the node's bundle.
field_attach_load() then loads the 'subtitle' and 'photo' fields
because they are both attached to the 'node' bundle 'article'.

Field definitions are represented as an array of key/value pairs.

array $field:
- id (integer, read-only): The primary identifier of the field. It is
  assigned automatically by field_create_field().
- field_name (string): The name of the field. Each field name is unique
  within Field API. When a field is attached to an entity, the field's data
  is stored in $entity->$field_name. Maximum length is 32 characters.
- type (string): The type of the field, such as 'text' or 'image'. Field
  types are defined by modules that implement hook_field_info().
- entity_types (array): The array of entity types that can hold instances
  of this field. If empty or not specified, the field can have instances
  in any entity type.
- cardinality (integer): The number of values the field can hold. Legal
  values are any positive integer or FIELD_CARDINALITY_UNLIMITED.
- translatable (integer): Whether the field is translatable.
- locked (integer): Whether or not the field is available for editing. If
  TRUE, users can't change field settings or create new instances of the
  field in the UI. Defaults to FALSE.
- module (string, read-only): The name of the module that implements the
  field type.
- active (integer, read-only): TRUE if the module that implements the field
  type is currently enabled, FALSE otherwise.
- deleted (integer, read-only): TRUE if this field has been deleted, FALSE
  otherwise. Deleted fields are ignored by the Field Attach API. This
  property exists because fields can be marked for deletion but only
  actually destroyed by a separate garbage-collection process.
- columns (array, read-only): An array of the Field API columns used to
  store each value of this field. The column list may depend on field
  settings; it is not constant per field type. Field API column
  specifications are exactly like Schema API column specifications but,
  depending on the field storage module in use, the name of the column may
  not represent an actual column in an SQL database.
- indexes (array): An array of indexes on data columns, using the same
  definition format as Schema API index specifications. Only columns that
  appear in the 'columns' setting are allowed. Note that field types can
  specify default indexes, which can be modified or added to when
  creating a field.
- foreign keys: (optional) An associative array of relations, using the same
  structure as the 'foreign keys' definition of hook_schema(). Note,
  however, that the field data is not necessarily stored in SQL. Also, the
  possible usage is limited, as you cannot specify another field as
  related, only existing SQL tables, such as filter formats.
- settings (array): A sub-array of key/value pairs of field-type-specific
  settings. Each field type module defines and documents its own field
  settings.
- storage (array): A sub-array of key/value pairs identifying the storage
  backend to use for the for the field:
  - type (string): The storage backend used by the field. Storage backends
    are defined by modules that implement hook_field_storage_info().
  - module (string, read-only): The name of the module that implements the
    storage backend.
  - active (integer, read-only): TRUE if the module that implements the
    storage backend is currently enabled, FALSE otherwise.
  - settings (array): A sub-array of key/value pairs of settings. Each
    storage backend defines and documents its own settings.

Field instance definitions are represented as an array of key/value pairs.

array $instance:
- id (integer, read-only): The primary identifier of this field instance.
  It is assigned automatically by field_create_instance().
- field_id (integer, read-only): The foreign key of the field attached to
  the bundle by this instance. It is populated automatically by
  field_create_instance().
- field_name (string): The name of the field attached to the bundle by this
  instance.
- entity_type (string): The name of the entity type the instance is attached
  to.
- bundle (string): The name of the bundle that the field is attached to.
- label (string): A human-readable label for the field when used with this
  bundle. For example, the label will be the title of Form API elements
  for this instance.
- description (string): A human-readable description for the field when
  used with this bundle. For example, the description will be the help
  text of Form API elements for this instance.
- required (integer): TRUE if a value for this field is required when used
  with this bundle, FALSE otherwise. Currently, required-ness is only
  enforced during Form API operations, not by field_attach_load(),
  field_attach_insert(), or field_attach_update().
- default_value_function (string): The name of the function, if any, that
  will provide a default value.
- default_value (array): If default_value_function is not set, then fixed
  values can be provided.
- deleted (integer, read-only): TRUE if this instance has been deleted,
  FALSE otherwise. Deleted instances are ignored by the Field Attach API.
  This property exists because instances can be marked for deletion but
  only actually destroyed by a separate garbage-collection process.
- settings (array): A sub-array of key/value pairs of field-type-specific
  instance settings. Each field type module defines and documents its own
  instance settings.
- widget (array): A sub-array of key/value pairs identifying the Form API
  input widget for the field when used by this bundle:
  - type (string): The type of the widget, such as text_textfield. Widget
    types are defined by modules that implement hook_field_widget_info().
  - settings (array): A sub-array of key/value pairs of
    widget-type-specific settings. Each field widget type module defines
    and documents its own widget settings.
  - weight (float): The weight of the widget relative to the other elements
    in entity edit forms.
  - module (string, read-only): The name of the module that implements the
    widget type.
- display (array): A sub-array of key/value pairs identifying the way field
  values should be displayed in each of the entity type's view modes, plus
  the 'default' mode. For each view mode, Field UI lets site administrators
  define whether they want to use a dedicated set of display options or the
  'default' options to reduce the number of displays to maintain as they
  add new fields. For nodes, on a fresh install, only the 'teaser' view
  mode is configured to use custom display options, all other view modes
  defined use the 'default' options by default. When programmatically
  adding field instances on nodes, it is therefore recommended to at least
  specify display options for 'default' and 'teaser':
  - default (array): A sub-array of key/value pairs describing the display
    options to be used when the field is being displayed in view modes
    that are not configured to use dedicated display options:
    - label (string): Position of the label. 'inline', 'above' and
      'hidden' are the values recognized by the default 'field' theme
      implementation.
    - type (string): The type of the display formatter, or 'hidden' for
      no display.
    - settings (array): A sub-array of key/value pairs of display
      options specific to the formatter.
    - weight (float): The weight of the field relative to the other entity
      components displayed in this view mode.
    - module (string, read-only): The name of the module which implements
      the display formatter.
  - some_mode: A sub-array of key/value pairs describing the display
    options to be used when the field is being displayed in the 'some_mode'
    view mode. Those options will only be actually applied at run time if
    the view mode is not configured to use default settings for this bundle:
    - ...
  - other_mode:
    - ...

The (default) render arrays produced for field instances are documented at
field_attach_view().

Bundles are represented by two strings, an entity type and a bundle name.

- @link field_types Field Types API @endlink. Defines field types,
  widget types, and display formatters. Field modules use this API
  to provide field types like Text and Node Reference along with the
  associated form elements and display formatters.

- @link field_crud Field CRUD API @endlink. Create, updates, and
  deletes fields, bundles (a.k.a. "content types"), and instances.
  Modules use this API, often in hook_install(), to create
  custom data structures.

- @link field_attach Field Attach API @endlink. Connects entity
  types to the Field API. Field Attach API functions load, store,
  generate Form API structures, display, and perform a variety of
  other functions for field data connected to individual entities.
  Fieldable entity types like node and user use this API to make
  themselves fieldable.

- @link field_info Field Info API @endlink. Exposes information
  about all fields, instances, widgets, and related information
  defined by or with the Field API.

- @link field_storage Field Storage API @endlink. Provides a
  pluggable back-end storage system for actual field data. The
  default implementation, field_sql_storage.module, stores field data
  in the local SQL database.

- @link field_purge Field API bulk data deletion @endlink. Cleans
  up after bulk deletion operations such as field_delete_field()
  and field_delete_instance().

- @link field_language Field language API @endlink. Provides native
  multilingual support for the Field API.
```

## Members (derived, 40)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [_field_extra_fields_pre_render()](../modules/field/field.module/_field_extra_fields_pre_render.md) (function) — Pre-render callback to adjust weights and visibility of non-field elements.
- [_field_filter_items()](../modules/field/field.module/_field_filter_items.md) (function) — Helper function to filter out empty field values.
- [_field_filter_xss_allowed_tags()](../modules/field/field.module/_field_filter_xss_allowed_tags.md) (function) — List of tags allowed by field_filter_xss().
- [_field_filter_xss_display_allowed_tags()](../modules/field/field.module/_field_filter_xss_display_allowed_tags.md) (function) — Human-readable list of allowed tags, for display in help texts.
- [_field_sort_items()](../modules/field/field.module/_field_sort_items.md) (function) — Helper function to sort items in a field according to user drag-n-drop reordering.
- [_field_sort_items_helper()](../modules/field/field.module/_field_sort_items_helper.md) (function) — Sort function for items order. (copied form element_sort(), which acts on #weight keys)
- [_field_sort_items_value_helper()](../modules/field/field.module/_field_sort_items_value_helper.md) (function) — Same as above, using ['_weight']['#value']
- [field_access()](../modules/field/field.module/field_access.md) (function) — Determine whether the user has access to a given field.
- [field_associate_fields()](../modules/field/field.module/field_associate_fields.md) (function) — Allows a module to update the database for fields and columns it controls.
- [field_bundle_settings()](../modules/field/field.module/field_bundle_settings.md) (function) — Gets or sets administratively defined bundle settings.
- [field_cache_clear()](../modules/field/field.module/field_cache_clear.md) (function) — Clear the field info and field data caches.
- [field_cron()](../modules/field/field.module/field_cron.md) (function) — Implements hook_cron().
- [field_extra_fields_get_display()](../modules/field/field.module/field_extra_fields_get_display.md) (function) — Returns the display settings to use for pseudo-fields in a given view mode.
- [field_extract_bundle()](../modules/field/field.module/field_extract_bundle.md) (function) — Helper function to extract the bundle name of from a bundle object.
- [field_filter_xss()](../modules/field/field.module/field_filter_xss.md) (function) — Like filter_xss_admin(), but with a shorter list of allowed tags.
- [field_flush_caches()](../modules/field/field.module/field_flush_caches.md) (function) — Implements hook_flush_caches().
- [field_get_default_value()](../modules/field/field.module/field_get_default_value.md) (function) — Helper function to get the default value for a field on an entity.
- [field_get_display()](../modules/field/field.module/field_get_display.md) (function) — Returns the display settings to use for an instance in a given view mode.
- [field_get_items()](../modules/field/field.module/field_get_items.md) (function) — Returns the field items in the language they currently would be displayed.
- [field_has_data()](../modules/field/field.module/field_has_data.md) (function) — Determine whether a field has any data.
- [field_help()](../modules/field/field.module/field_help.md) (function) — Implements hook_help().
- [field_modules_disabled()](../modules/field/field.module/field_modules_disabled.md) (function) — Implements hook_modules_disabled().
- [field_modules_enabled()](../modules/field/field.module/field_modules_enabled.md) (function) — Implements hook_modules_enabled().
- [field_permission()](../modules/field/field.module/field_permission.md) (function) — Implements hook_permission().
- [field_sync_field_status()](../modules/field/field.module/field_sync_field_status.md) (function) — Refreshes the 'active' and 'storage_active' columns for fields.
- [field_system_info_alter()](../modules/field/field.module/field_system_info_alter.md) (function) — Implements hook_system_info_alter().
- [field_theme()](../modules/field/field.module/field_theme.md) (function) — Implements hook_theme().
- [field_ui_menu_load()](../modules/field_ui/field_ui.module/field_ui_menu_load.md) (function) — Menu loader; Load a field instance based on field and bundle name.
- [field_view_field()](../modules/field/field.module/field_view_field.md) (function) — Returns a renderable array for the value of a single field in an entity.
- [field_view_mode_settings()](../modules/field/field.module/field_view_mode_settings.md) (function) — Returns view mode settings in a given bundle.
- [field_view_value()](../modules/field/field.module/field_view_value.md) (function) — Returns a renderable array for a single field value.
- [template_preprocess_field()](../modules/field/field.module/template_preprocess_field.md) (function) — Theme preprocess function for theme_field() and field.tpl.php.
- [template_process_field()](../modules/field/field.module/template_process_field.md) (function) — Theme process function for theme_field() and field.tpl.php.
- [FIELD_BEHAVIOR_CUSTOM](../modules/field/field.module/_file.md#field_behavior_custom) (constant) — Value for field API indicating a widget can receive several field values.
- [FIELD_BEHAVIOR_DEFAULT](../modules/field/field.module/_file.md#field_behavior_default) (constant) — Value for field API concerning widget default and multiple value settings.
- [FIELD_BEHAVIOR_NONE](../modules/field/field.module/_file.md#field_behavior_none) (constant) — Value for field API indicating a widget doesn't accept default values.
- [FIELD_CARDINALITY_UNLIMITED](../modules/field/field.module/_file.md#field_cardinality_unlimited) (constant) — Value for field API indicating a field accepts an unlimited number of values.
- [FIELD_LOAD_CURRENT](../modules/field/field.module/_file.md#field_load_current) (constant) — Age argument for loading the most recent version of an entity's field data with field_attach_load().
- [FIELD_LOAD_REVISION](../modules/field/field.module/_file.md#field_load_revision) (constant) — Age argument for loading the version of an entity's field data specified in the entity with field_attach_load().
- [FieldUpdateForbiddenException](../modules/field/field.module/FieldUpdateForbiddenException.md) (class) — Exception class thrown by hook_field_update_forbid().

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
