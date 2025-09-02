# Product Store Website

## Overview

This is a Django-based product listing website that allows users to browse products, view detailed product information, and manage products through Django admin. The application serves as a foundation for an e-commerce platform with plans for future cart and checkout functionality. It's designed to run on both local machines and cloud platforms like Replit.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Web Framework
- **Django 5.2.5**: Chosen as the primary web framework for rapid development and built-in admin functionality
- **Model-View-Template (MVT) Pattern**: Standard Django architecture separating data models, business logic, and presentation layers

### Frontend Architecture
- **Bootstrap 5.1.3**: CSS framework for responsive design and pre-built UI components
- **Template-based Rendering**: Server-side HTML generation using Django templates
- **Static Asset Management**: Django's static file handling for CSS, JS, and media files

### Data Layer
- **SQLite Database**: Default Django database for simplicity and portability
- **Django ORM**: Object-relational mapping for database operations
- **Model Design**: Single Product model with fields for name, slug, description, price, image, and timestamps

### URL Routing
- **URL Configuration**: Hierarchical URL patterns with slug-based product detail pages
- **Named URLs**: Use of Django's named URL patterns for maintainable links
- **SEO-Friendly URLs**: Slug-based URLs for better search engine optimization

### Content Management
- **Django Admin Interface**: Built-in admin panel for product management
- **Custom Admin Configuration**: Enhanced admin interface with search, filters, and list display
- **Auto-slug Generation**: Automatic URL slug creation from product names

### File Handling
- **Media File Management**: Django's media handling for product images
- **Image Upload**: Support for product image uploads to 'products/' directory
- **Static File Serving**: Development-mode static file serving configuration

### Application Structure
- **Single App Architecture**: Products app containing all core functionality
- **Management Commands**: Custom Django management command for populating sample data
- **Migration System**: Django's database migration system for schema management

### Template System
- **Template Inheritance**: Base template with block inheritance for consistent layout
- **Responsive Design**: Mobile-first responsive design using Bootstrap grid system
- **Template Context**: Clean separation of data and presentation logic

## External Dependencies

### Frontend Libraries
- **Bootstrap 5.1.3**: CSS framework loaded via CDN for styling and responsive layout
- **Bootstrap JavaScript**: Interactive components and utilities

### Python Packages
- **Django 5.2.5**: Core web framework
- **Pillow**: Image processing library for handling product images (implied by ImageField usage)

### Static Resources
- **CDN Dependencies**: Bootstrap CSS and JS loaded from jsDelivr CDN
- **Media Storage**: Local file system storage for uploaded product images

### Development Tools
- **Django Development Server**: Built-in development server for local testing
- **Django Admin**: Built-in administrative interface for content management
- **Django Management Commands**: Custom commands for data population and maintenance

The architecture is designed for simplicity and rapid development while maintaining the flexibility to add e-commerce features like shopping cart, user authentication, and payment processing in future iterations.