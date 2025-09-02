# Product Store Website

## Overview

This is a comprehensive Django-based e-commerce website that provides complete online shopping functionality. Users can browse products, manage shopping carts, create accounts, place orders, and track their purchase history. The application includes user authentication, order management, and an intuitive admin interface for product and order management. It's designed to run on both local machines and cloud platforms like Replit.

## Current Status

✅ **Phase 1 Complete**: Basic product listing with Django admin  
✅ **Phase 2 Complete**: Categories, search, filtering, pagination, and shopping cart  
✅ **Phase 3 Complete**: User authentication and order tracking system  
🔄 **Phase 4 In Progress**: Advanced features and polish

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
- **Model Design**: 
  - **Product Model**: Core product information with category relationships
  - **Category Model**: Product categorization system with slug-based URLs
  - **UserProfile Model**: Extended user information (phone, address, date of birth)
  - **Order Model**: Complete order tracking with status management
  - **OrderItem Model**: Individual items within orders with pricing history

### URL Routing
- **URL Configuration**: Hierarchical URL patterns with slug-based product detail pages
- **Named URLs**: Use of Django's named URL patterns for maintainable links
- **SEO-Friendly URLs**: Slug-based URLs for better search engine optimization

### Content Management
- **Django Admin Interface**: Comprehensive admin panel for products, categories, users, and orders
- **Custom Admin Configuration**: Enhanced admin interface with search, filters, list display, and inline editing
- **Auto-slug Generation**: Automatic URL slug creation from product and category names
- **Order Management**: Full order tracking and status management through admin interface

### File Handling
- **Media File Management**: Django's media handling for product images
- **Image Upload**: Support for product image uploads to 'products/' directory
- **Static File Serving**: Development-mode static file serving configuration

### Application Structure
- **Multi-App Architecture**: 
  - **Products App**: Core product management, cart functionality, and guest checkout
  - **Accounts App**: User authentication, profiles, order tracking, and authenticated checkout
- **Management Commands**: Custom Django management commands for populating sample data and categories
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

### Authentication & User Management
- **User Registration**: Custom registration form with profile creation
- **User Authentication**: Login/logout functionality with session management
- **User Profiles**: Extended user information with editable profiles
- **Order Tracking**: Complete order history with detailed order views
- **Dual Checkout**: Support for both guest and authenticated user checkout flows

### Recent Changes (September 2, 2025)
- **Added User Authentication System**: Complete registration, login, and profile management
- **Implemented Order Tracking**: Full order management with status tracking and history
- **Enhanced Navigation**: Dynamic navigation with user-specific menu options
- **Dual Checkout System**: Separate checkout flows for guests and authenticated users
- **Admin Enhancements**: Added user profile and order management in Django admin
- **Template Updates**: Responsive authentication templates with Bootstrap styling

The architecture now provides a complete e-commerce foundation with user management, order tracking, and the flexibility to add advanced features like payment processing, inventory management, and customer analytics in future iterations.